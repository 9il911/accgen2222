import os
import wget
import string
#from PIL import Image
from base64 import b64decode
#from hashlib import sha1
from os import system
from io import BytesIO
import names
import base64
import hmac
import time
import json
from hashlib import sha1
import secmail
import random
import platform,socket,re,uuid
import json
#import webbrowser
import requests
from time import sleep
from bs4 import BeautifulSoup
from time import time as timestamp
from fancy_text import fancy
import os
#os.system('pip install pymongo')
#os.system('pip install dnspython amino_new.py')
import dns.resolver
#dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
#dns.resolver.default_resolver.nameservers=['8.8.8.8']
import json
from pymongo import MongoClient
import urllib.parse
from python_rucaptcha import ImageCaptcha
import ssl
import heroku3
from os import path
def restart():
    key='e36bb985-e2f1-43fd-b85e-e4569be5d05b'
    app_name="accgen123"
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[app_name]
    botapp.restart()
uname='sirlezhacker'
pas='3vc1r@2'
mongo= MongoClient("mongodb+srv://"+urllib.parse.quote_plus(uname)+":"+urllib.parse.quote_plus(pas)+"@cluster0.hhsm1.mongodb.net/test",ssl_cert_reqs=ssl.CERT_NONE)
c=mongo['amino']
db=c["acc_gen"]
def gen_captcha():
    val = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + "_-", k=462)).replace("--", "-")
    return val
def device():
        headers = {
    'Host': 'aminoapps.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://aminoapps.com',
    }
 
        data = {
        "recaptcha_challenge": gen_captcha(),
        "recaptcha_version":"v3",
        "auth_type":0,
        "secret":"samar123",
        "email":"p5y3xagz@wwjmp.com"
        }
        data=(data)
        req = requests.post('https://aminoapps.com/api/auth', headers=headers, json=data)
        req=json.loads(req.text)
        devid=req['result']['url'].split('=')[4]
        dev=devid.upper()
        return dev
def code(link):

    user_answer=ImageCaptcha.ImageCaptcha(rucaptcha_key=str("0bea597111a8d2230504e76f413268fb")).captcha_handler(captcha_link=link)
    return user_answer["captchaSolve"]
 
def gen_email():
    mail = secmail.SecMail()
    email = mail.generate_email()
    return email
    
def upload(url):
    link = requests.get(url)
    result = BytesIO(link.content)
    return result
 
def get_message(email):
                try:
                    sleep(4)
                    f=email
                    mail = secmail.SecMail()
                    inbox = mail.get_messages(f)
                    print('done')
                    for Id in inbox.id:
                        msg = mail.read_message(email=f, id=Id).htmlBody
                        bs = BeautifulSoup(msg, 'html.parser')
                        images = bs.find_all('a')[0]
                        url = (images['href']+'\n')
                        if url is not None:
                         print('Vrification Url\n')
                         #print(url)
                         return url
                         #wget.download(url=url,out="code.png")
                except:
                    pass
def hwid():
    return names.get_full_name()+str(random.randint(0,10000000))+platform.version()+platform.machine()+names.get_first_name()+socket.gethostbyname(socket.gethostname())+':'.join(re.findall('..', '%012x' % uuid.getnode()))+platform.processor()
def sig(data):
        mac = hmac.new(bytes.fromhex("307c3c8cd389e69dc298d951341f88419a8377f4"), data.encode("utf-8"), sha1)
        digest = bytes.fromhex("22") + mac.digest()
        return base64.b64encode(digest).decode("utf-8")
  
            
def register(nickname: str, email: str, password: str,deviceId: str,verificationCode: str):
        data = {
            "secret": f"0 {password}",
            "deviceID": deviceId,
            "email": email,
            "clientType": 100,
            "nickname": nickname,
            "latitude": 0,
            "longitude": 0,
            "address": None,
            "clientCallbackURL": "narviiapp://relogin",
            "validationContext": {
                "data": {
                    "code": verificationCode
                },
                "type": 1,
                "identity": email
            },
            "type": 1,
            "identity": email,
            "timestamp": int(timestamp() * 1000)
        }
        heads={
    'Accept-Language': 'en-US', 
    'Content-Type': 'application/json; charset=utf-8', 
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.3.33180)', 
    'Host': 'service.narvii.com', 
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
    }
        data=json.dumps(data)
        heads["NDC-MSG-SIG"]=sig(data)
        heads["Content-Length"] = str(len(data))
        heads["NDCDEVICEID"]=deviceId
        response = requests.post(f"https://service.narvii.com/api/v1/g/s/auth/register", data=data, headers=heads)
        if response.json()['api:message'] == "OK":
            secret=response.json()['secret']
            d={}
            #with open ("new.txt","a") as f:
            d["email"]=str(email)
            d["password"]=str(password)
            d["device"]=str(deviceid)
            d['secret']=str(secret)
            db.insert_one(d)
        
        #print(response.text)
def request_verify_code(email: str,deviceId: str):
        data = {
            "identity": email,
            "type": 1,
            "deviceID": deviceId
        }
        heads={
    'Accept-Language': 'en-US', 
    'Content-Type': 'application/json; charset=utf-8', 
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.3.33180)', 
    'Host': 'service.narvii.com', 
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
        }
        data = json.dumps(data)
        heads["Content-Length"] = str(len(data))
        heads["NDCDEVICEID"]=deviceId
        heads["NDC-MSG-SIG"]=sig(data)
        
        response = requests.post(f"https://service.narvii.com/api/v1/g/s/auth/request-security-validation", data=data, headers=heads)
        print(response.text)
        #if response.json()['api:message'] != "OK":
 
 
def verify(values):
        imgs=get_message(values)
        sleep(1)
        #print(imgs)
        verifycode=code(imgs)
        #print(code)
        return verifycode
 
 
 
        
        
 
def geticon(client):
    r=random.randint(0, 98)
    url=client.get_all_users(size=100).profile.icon[r]
    if url is None:
        geticon(client)
    elif url=="None":
        geticon(client)
    else:
        return url
    
def set_acc(email):
    client.login(email, password)
    url=geticon(client)
    try:
         client.edit_profile(icon=upload(url))
    except:
        pass
    client.join_community(comId="226547416")
 
def fancy_name():
    nm=''
    for i in names.get_first_name():
        n=random.randint(1, 5)
        if n==1:
            nm+=fancy.bold(i)
        if n==2:
            nm+=fancy.light(i)
        if n==3:
            nm+=fancy.box(i)
        if n==4:
            nm+=fancy.sorcerer(i)
        if n==5:
            nm+=i
    return nm
    
#no=int(input("how many accounts to create:  "))
password='tempmail'
 
for _ in range(5):
    deviceid=device()
    #print(deviceid)
    #saveemail="echo "+deviceid+">>devused.txt"
    
    print('------------------------------')
    values=gen_email()
    email=values
    print(email)
    #print(pas)
    nick=names.get_first_name()
    req=request_verify_code(email=email, deviceId=deviceid)
    vcode=verify(values)
    print(vcode)
    register(nickname=nick, email=email, password=password,deviceId=deviceid,verificationCode=vcode)
    
restart()
