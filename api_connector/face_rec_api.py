
import requests
import utility.logger
class Face_api:
    
    def check_image(img):
        headers = { 'content-type':'application/json'}
        data = {'img':img}
        url = 'http://172.20.10.2/rest/logic/checkFace'
        res = requests.post(url,headers=headers,data= str(data).replace('\'','\"'))
        if res.status_code == 200:
            return res.json()
