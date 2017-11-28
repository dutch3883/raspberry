# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from api_connector.face_rec_api import Face_api
import cv

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
 
# allow the camera to warmup
time.sleep(0.1)
 
#cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#cv2.resizeWindow('image',600,600)
# grab an image from the camera
while True:
    rawCapture = PiRGBArray(camera)
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    print(image)
    img= cv.resize(image,(600,600),interpolation=cv.INTER_AREA)
    # display the image on screen and wait for a keypress
    cv.waitKey(10)
    print('check')
