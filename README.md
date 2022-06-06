# Windows Version

A functional face recognizer made with Python and libs for image detection. This version will be converted to run in a raspberry pi model 3b.

## How do I run?


1. upgrade your pip to avoid errors during installation.
    ```pip install --upgrade pip```
&nbsp;
2. Install face recognition. 
    ```https://www.geeksforgeeks.org/how-to-install-face-recognition-in-python-on-windows/```
&nbsp;
3. install pickle.
    ```pip install pickle-mixin```
&nbsp;
4. install opencv.
    ```pip install opencv-python```
&nbsp;
5. install imutils.
    ```pip install imutils```
&nbsp;
6. create a folder in `database` with the respective name you want to recognize.
&nbsp;
7. run **`faceShot.py`**, type the same name as the folder you created earlier.
&nbsp;
8. run **`imageTraining.py`** to encode and serialize all the images.
&nbsp;
9. run **`faceDetection.py`** to test if the registered face is being recognized.