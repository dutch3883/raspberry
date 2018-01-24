import cognitive_face as CF
import json
import requests
import traceback
#import logger
import time

site_url   = 'http://ddfacematch.azurewebsites.net'
#site_url = 'http://172.20.10.2'


def __load_key():
    with open('../config.json','r') as config_file:
        config = json.load(config_file)
    return config['key']


key = __load_key()
CF.Key.set(key)
Base_url = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(Base_url)


def check_image(img):
    return _check_image_diy(img)


    
def _check_image_azure(img):
    pass
    
def _check_image_diy(img):
    headers = { 'Content-Type':'application/json'}
    data = {'img':img.decode('utf-8')}
    url = site_url+'/rest/logic/checkFace'
    res = requests.post(url,headers=headers,json=data)
    #print(str(data).replace('\'','\"'))
    if res.status_code == 200:
        return res.json()
    else:
        print('error: ',res.json())

if __name__ == '__main__':
    time_req = time.time()
    try:

        user = {"fname": "ภาณุวัชร์", "lname": "Boonyasup", "status": "guest"}
        g = json.dumps(user, ensure_ascii=False)
        res =CF.person.create('v1_0', 'Panuwach', json.dumps(user))
        print(res)
        time_res = time.time()
        print("response {} with time= {:.3f} sec".format(res, (time_res - time_req)))

    except Exception as e:
        print(traceback.format_exc())
