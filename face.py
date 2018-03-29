from picamera import PiCamera
import time
import requests
import base64
import RPi.GPIO

def getaccess_token():
    host='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=t7NNK8h4xGoAHuTpbwyo9qYC&client_secret=MBg0AK0PhiOhytA35rSQbSa4boIQsdz3'
    header_1 = {'Content-Type':'application/json; charset=UTF-8'}
    request=requests.post(host,headers =header_1)
    access_token=request.json()['access_token']
    return access_token

def take_picture():

    camera.start_preview()
    time.sleep(2)
    camera.capture('image.jpg')
    camera.stop_preview()

def open_pic():
    f = open('image.jpg', 'rb')
    img = base64.b64encode(f.read())
    return img

def go_api(img,access_token):
    data_1 = {"image":img,'group_id':'asd'}
    params_1 = {'access_token':access_token}
    header_2 = {'Content-Type':'application/x-www-form-urlencoded'}
    pic_re=requests.post('https://aip.baidubce.com/rest/2.0/face/v2/identify',params=params_1,headers=header_2,data=data_1)
    print(len(pic_re.text))
    if len(pic_re.text)>130:
        if pic_re.json()['result'][0]['scores'][0]>75:
            return ('yes')
        else :
            return ('no')

    else:
        print('error')
        return ('no')
    #return(pic_re.json()['result'][0]['scores'])
def led():
    RPi.GPIO.output(18, True)
    time.sleep(10)
    RPi.GPIO.output(18, False)

if __name__ == '__main__':
    RPi.GPIO.setmode(RPi.GPIO.BCM)
    RPi.GPIO.setup(18, RPi.GPIO.OUT)
    camera = PiCamera()
    access_token=getaccess_token()
    while True :
        take_picture()
        img=open_pic()
        a=go_api(img,access_token)
        if a=='yes':
            led()
        if a=='no':
            pass
