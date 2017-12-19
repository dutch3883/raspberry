
import requests
#import logger
site_url   = 'http://ddfacematch.azurewebsites.net'
def check_image(img):
    headers = { 'Content-Type':'application/json'}
    data = {'img':img}
    url = site_url+'/rest/logic/checkFace'
    res = requests.post(url,headers=headers,json=data)
    #print(str(data).replace('\'','\"'))
    if res.status_code == 200:
        return res.json()
    else:
        print('error: ',res.json())
