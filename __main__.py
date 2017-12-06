# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import base64
from raspberry import api
def routine():
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.vflip = False
    camera.resolution = (500,500)
    camera.capture('Image.jpg')
    with open("Image.jpg","rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    time_req = time.time()
    response = api.check_image(encoded_string)
    time_res = time.time()
    print("have response {} with time= {:.3f} sec".format(response,(time_res-time_req)))
    
if __name__ == '__main__':
    while True:
        routine()


