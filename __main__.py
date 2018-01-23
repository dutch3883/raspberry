# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import datetime
import base64
import os
from raspberry import api
def routine():
    # initialize the camera and grab a reference to the raw camera capture
    with PiCamera() as camera:
        camera.vflip = True
        camera.resolution = (500,500)
        img_name = 'Image'+str(os.getpid())+datetime.datetime.now().strftime('_%Y-%m-%d %H:%M:%S')+'.jpg'
        camera.capture(img_name)
    with open(img_name,"rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    time_req = time.time()
    response = api.check_image(encoded_string)
    time_res = time.time()
    if not response:
        try:
            os.remove(img_name)
        except Exception:
            pass
    else:
        os.rename('found/'+img_name)
    print("pid {} have response {} with time= {:.3f} sec".format(os.getpid(),response,(time_res-time_req)))
    os._exit(0)
    
if __name__ == '__main__':
   for i in range(10):
        newpid = os.fork()
        if newpid == 0:
            routine()
        else:
            print("parent: {}, child:{} ".format(os.getpid(), newpid))
            
        time.sleep(1)
       
   


