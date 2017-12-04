# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import base64
#from api_connector import check_image
from api_connector import check_image

def routine():
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.vflip = False
    camera.resolution = (500,500)
    camera.capture('Image.jpg')
    with open("Image.jpg","rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    response = check_image(encoded_string)
    print(response)
    # allow the camera to warmup
    

    #cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('image',600,600)
    # grab an image from the camera
    #rawCapture = PiRGBArray(camera)
##    while True:
##        rawCapture = PiRGBArray(camera)
##        print(rawCapture)
##        # display the image on screen and wait for a keypress
##        #Face_api.check_image(rawCapture)
##        print('check')
##        
if __name__ == '__main__':
    routine()


