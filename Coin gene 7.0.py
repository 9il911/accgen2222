cid ="130217628"
import os
import sys
from keep_alive import keep_alive
os.system("pip install Dick.py==1.3.5")
import pyfiglet
import colorama
import pytz
from colorama import init, Fore, Back, Style
print("\n\n\33[48;5;5m\33[38;5;234m ❮ COIN GENERATOR 7.0 ❯ \33[0m\33[48;5;235m\33[38;5;5m \33[0m")
init()
print(Fore.GREEN + Style.BRIGHT)
print(pyfiglet.figlet_format("TECH", font="cybermedium"))
print(pyfiglet.figlet_format("VISION", font="cybermedium"))
keep_alive()
import amino
import random
from uuid import uuid4
import requests
import threading
import time
import random
from hmac import new
from os import urandom
from hashlib import sha1
import base64
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from os import path
import json
THIS_FOLDER = path.dirname(path.abspath(__file__))
deviceIdfile = path.join(THIS_FOLDER, "device")
cc=open("list2.txt","w")
os.remove("list2.txt")
dh=[]
tz = pytz.timezone('Asia/Kolkata')
now = datetime.now(tz)
current_time=now.strftime("%H:%M")
print(current_time)
if "24:00" in current_time:
	os.remove("list.txt")
n=10	
emf=open("accounts.json")
dh=json.load(emf)
for i in range((len(dh) + n - 1) // n):
	x=dh[i:i+n]
	fp=open(f"ac{i+1}.json","w")
	xy=json.dump(x,fp)
	fp.close()

x=((len(dh) + n - 1) // n)

vg=list(range(1,x+2))

for yt in vg:
	hu=open("list2.txt","a")
	hu.write(str(yt)+"\n")
def rnf():
	try:
		z=random.randint(1,x)
		g=open("list.txt","r")
		pyt=(g.read())
		if str(z) not in pyt:
			g=open("list.txt","a")		
			g.write(str(z)+"\n")
			return str(z)
		else:
			rnf()
	except:
		os.remove("list.txt")
		file=open("list.txt","w")
		os.execv(sys.executable, ['python'] + sys.argv)

rnf()
io=open("list2.txt","r")
iot=(io.readlines())
g=open("list.txt","r")
pt=(g.readlines())

set_difference = set(iot) - set(pt)
ld = list(set_difference)

nl=[]

for xf in ld:
    nl.append(xf.replace("\n", ""))
    
def t():
	for xf in range(1):
		try:
			return (nl[xf])
		except:
			os.remove("new2.txt")
			file=open("new2.txt","w")
			os.execv(sys.executable, ['python'] + sys.argv)
		
dts=t()

emailfile=(f"ac{dts}.json")
	
dictlist=[]

with open(emailfile) as f:
    dictlist = json.load(f)
headers={
        "cookies":"__cfduid=d0c98f07df2594b5f4aad802942cae1f01619569096",
        "authorization":"Basic NWJiNTM0OWUxYzlkNDQwMDA2NzUwNjgwOmM0ZDJmYmIxLTVlYjItNDM5MC05MDk3LTkxZjlmMjQ5NDI4OA=="
    }
 
def tapcoins(usrd:str):
    data = {
        "reward":{"ad_unit_id":"t00_tapjoy_android_master_checkinwallet_rewardedvideo_322","credentials_type":"publisher","custom_json":{"hashed_user_id":f"{usrd}"},"demand_type":"sdk_bidding","event_id":None,"network":"facebook","placement_tag":"default","reward_name":"Amino Coin","reward_valid":"true","reward_value":2,"shared_id":"dc042f0c-0c80-4dfd-9fde-87a5979d0d2f","version_id":"1569147951493","waterfall_id":"dc042f0c-0c80-4dfd-9fde-87a5979d0d2f"},
        "app":{"bundle_id":"com.narvii.amino.master","current_orientation":"portrait","release_version":"3.4.33567","user_agent":"Dalvik\/2.1.0 (Linux; U; Android 10; G8231 Build\/41.2.A.0.219; com.narvii.amino.master\/3.4.33567)"},"date_created":1620295485,"session_id":"49374c2c-1aa3-4094-b603-1cf2720dca67","device_user":{"country":"US","device":{"architecture":"aarch64","carrier":{"country_code":602,"name":"Vodafone","network_code":0},"is_phone":"true","model":"GT-S5360","model_type":"Samsung","operating_system":"android","operating_system_version":"29","screen_size":{"height":2260,"resolution":2.55,"width":1080}},"do_not_track":"false","idfa":"7495ec00-0490-4d53-8b9a-b5cc31ba885b","ip_address":"","locale":"en","timezone":{"location":"Asia\/Seoul","offset":"GMT+09:00"},"volume_enabled":"true"}
        }
    event=uuid4()
    data["reward"]["event_id"]=f"{event}"
    try:
        requests.post("https://ads.tapdaq.com/v4/analytics/reward",json=data, headers=headers)
    except:
    	pass


def device_Id_generator(identifier: str): 
	return ("32" + identifier.hex() + new(bytes.fromhex("76b4a156aaccade137b8b1e77b435a81971fbd3e"), b"\x32" + identifier, sha1).hexdigest()).upper()
	return thedevice

device_Id = device_Id_generator(identifier=urandom(20))
thedevicejs = {
    "device_id": f"{device_Id}",
    "device_id_sig": "Aa0ZDPOEgjt1EhyVYyZ5FgSZSqJt",
    "user_agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/beyond1qlteue-user 5; com.narvii.amino.master/3.4.33562)"
    }
deviceIdfile = open('device.json', "w")
json.dump(thedevicejs, deviceIdfile)
deviceIdfile.close()
client = amino.Client()

tzs = [-900, -800, -700, -600, -500, -400, -330, -300, -200, -100, 0, 100, 110, 120, 200, 300, 400, 500, 600, 700, 800, 900]

def magicnum():
    toime={"start":int(datetime.timestamp(datetime.now())),"end":int(datetime.timestamp(datetime.now()))+300}
    return toime

def sendobj(sub : amino.SubClient):
    timer=[
    magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum()
    ]
    tzs = [-900, -800, -700, -600, -500, -400, -330, -300, -200, -100, 0, 100, 110, 120, 200, 300, 400, 500, 600, 700, 800, 900]
    t=random.choice(tzs)
    sub.send_active_obj(timers=timer,tz=t)

def log(cli : amino.Client,email : str, password : str):
    try:
        cli.login(email=email,password=password)
        print(f"logged into {email}\n")
    except Exception:
        pass

def task(sub : amino.SubClient,email : str,i : int):
    try:
        sendobj(sub)
        print(f"Generated Coins for {email} times :- {i+1}")
    except:
        return None

def threadit(acc : dict):
    email=acc["email"]
    password=acc["password"]
    device=acc["device"]
    client=amino.Client(deviceId=device)
    log(cli=client,email=email,password=password)
    try:
    	os.remove("device.json")
    	client.join_community(cid)
    	subclient=amino.SubClient(comId=cid,profile=client.profile)
    	usrd=client.userId
    	with ThreadPoolExecutor(max_workers=1) as executorx:
    		_ = [executorx.submit(task, subclient,email,i)for i in range(500)]
    	for _ in range(500):
    		try:
    			threading.Thread(target=tapcoins,args=(usrd,)).start()
    			#print("Generating")
    		except:
    			pass
    	client.logout()
    	print(f"Generated Coins with {email}")
    except:
    	pass
def main():
    print(f"\n\33[93;5;5m\33[93;5;234m ❮ Total Accounts : {len(dh)} ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m")
    for amp in dictlist:
    	threadit(amp)
    print(f"\n\33[93;5;5m\33[93;5;234m ❮ Claimed coins from {len(dictlist)} accounts ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m")
    time.sleep(2)
 
if __name__ == '__main__':
	main()
	os.execv(sys.executable, ['python'] + sys.argv)
	