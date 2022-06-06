import cv2
import os
import tkinter as tk
from tkinter import simpledialog

#ROOT = tk.Tk()
def shot():
    name = USER_INP = simpledialog.askstring(title="Cadastro",
                                    prompt="Digite o nome da:")
                                    
    parent_dir = 'database'

    try:
        path = os.path.join(parent_dir, name)
        os.mkdir(path)
        pass
    except IOError:
        pass

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("pressione espaco para tirar a foto", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("pressione espaco para tirar a foto", 500, 300)

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("falha ao capturar o frame")
            break
        cv2.imshow("pressione espaco para tirar a foto", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:

            print("Escape hit, closing...")
            break
        elif k%256 == 32:

            img_name = "database/"+ name +"/image_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} salvo!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()