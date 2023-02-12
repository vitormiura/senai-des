from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
import requests

def main():
	currentname = "desconhecido"               
	encodingsP = "encodings.pickle"
	cascade = "haarcascade_frontalface_default.xml"

	def send_message(name):
		return requests.post(
			"your domain here",
			auth=("api", "your api here"),
			files = [("attachment", ("image.jpg", open("image.jpg", "rb").read()))],
			data={"from": 'example@example.com',
				"to": ["example@example.com"],
				"subject": "Aviso de presença",
				"html": "<html>" + name + " esteve presente.  </html>"})


	print("[INFO] loading encodings + face detector...")
	data = pickle.loads(open(encodingsP, "rb").read())
	detector = cv2.CascadeClassifier(cascade)
	
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()

	time.sleep(2.0)

	fps = FPS().start()

	while True:
		frame = vs.read()
		frame = imutils.resize(frame, width=500)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


		rects = detector.detectMultiScale(gray, scaleFactor=1.1, 
			minNeighbors=5, minSize=(30, 30),
			flags=cv2.CASCADE_SCALE_IMAGE)

		boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

		encodings = face_recognition.face_encodings(rgb, boxes)
		names = []

		for encoding in encodings:

			matches = face_recognition.compare_faces(data["encodings"],
				encoding)
			name = "desconhecido"


			if True in matches:

				matchedIdxs = [i for (i, b) in enumerate(matches) if b]
				counts = {}


				for i in matchedIdxs:
					name = data["names"][i]
					counts[name] = counts.get(name, 0) + 1

				name = max(counts, key=counts.get)
				

				if currentname != name:
					currentname = name
					print(currentname)

					img_name = "image.jpg"
					cv2.imwrite(img_name, frame)
					print('Taking a picture.')
					
					request = send_message(name)
					print ('Status: '+format(request.status_code)) #200 se funcionou
					

			names.append(name)


		for ((top, right, bottom, left), name) in zip(boxes, names):

			cv2.rectangle(frame, (left, top), (right, bottom),
				(0, 255, 225), 2)
			y = top - 15 if top - 15 > 15 else top + 15
			cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
				.8, (0, 255, 255), 2)


		cv2.imshow("App rodando", frame)
		key = cv2.waitKey(1) & 0xFF

		if key == ord("q"):
			break


		fps.update()


	fps.stop()
	print("Aberto por: {:.2f}".format(fps.elapsed()))
	print("Média de FPS: {:.2f}".format(fps.fps()))


	cv2.destroyAllWindows()
	vs.stop()
