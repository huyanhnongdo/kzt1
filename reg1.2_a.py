import os
import os, sys, re, json
from threading import Thread
import threading
import time
try:
   import requests
except:
   os.system('pip install requests')
   try:
     import requests
   except:
     print(sr+'Phiên Bản Termux Của Bạn Quá Cũ ')
     exit()
import random
from time import sleep
from datetime import datetime
from bs4 import BeautifulSoup as bs
from colorama import Fore
import datetime,base64
import random
from urllib.parse import unquote
from datetime import datetime
from time import sleep
os.system("cls" if os.name == "nt" else "clear")
jayztrick="\033[1;91m[\033[1;92m×͜×\033[1;91m] \033[1;97m=>"
dau="\033[1;91m[\033[1;92m×͜×\033[1;91m] \033[1;97m=>"
jayzthanh="\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
def banner():
 banner = f"""
\033[1;36m╔═══════════════════════════════════════════════════════════════╗
\033[1;36m║                                  \033[1;36m  ║\033[1;93m Copyright:\033[1;31m JayZ Trick  \033[1;36m  ║
\033[1;36m║                                  \033[1;36m  ║\033[1;93m Momo: \033[1;94m0978369023\033[1;36m         ║
\033[1;36m║\033[1;34m   █ ▄▀█ █▄█ ▀█ ▄▄ \033[1;97m▀█▀ █▀█ █▀█ █    \033[1;36m║\033[1;93m MB Bank : \033[1;96m056207003993   \033[1;36m║
\033[1;36m║\033[1;97m █▄█ █▀█  █  █▄   \033[1;93m  █  █▄█ █▄█ █▄▄ \033[1;36m ║\033[1;93m Donate: \033[1;92m0978369023\033[1;36m       ║
\033[1;36m║                                  \033[1;36m  ║\033[1;93m Zalo :\033[1;97m 0819847324\033[1;36m        ║
\033[1;36m║                                  \033[1;36m  ║\033[1;93m Support Tool: \033[1;95mJAYZ-TOOL  \033[1;36m║
\033[1;36m╚═══════════════════════════════════════════════════════════════╝
{jayzthanh}
{jayztrick}  \033[1;35mTOOL REG PAGE FACEBOOK VIP 
{jayztrick}  \033[1;34mCopyRight © : \033[1;33mJayZ Trick © 
{jayztrick}  \033[1;36mMua Key IB Zalo: \033[1;32m 0819847324 
{jayztrick}  \033[1;35mWeb Bán Key Tool: \033[1;37mjayztool.xyz
{jayzthanh}
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)



banner();
time = datetime.now()
a=time.strftime("%d")
h=int(time.strftime("%d"))
ngày_trc=h-1
b=time.strftime("%m")
day=time.strftime("%d-%m-%Y")
today=time.strftime("%d-%m-%Y")
d=time.strftime("%d-%m")
encodedBytes = base64.b64encode(d.encode("utf-8"))
key = str(encodedBytes, "utf-8")
long_url=(f"https://jayztool.tk/jayzkey.php/?key={key}")
api_token='2e2a3c8b826e0a9eaa1358125dbf4fb1006120f7'
url=requests.get(f'https://link1s.com/api?api={api_token}&url={long_url}').json()
status=url['status']
link=url['shortenedUrl']
#lấy key
file_key=f'key-ngày{a}.txt'
file_key_cũ=f'key-ngày{ngày_trc}.txt'
check_file_key=os.path.exists(file_key)
if check_file_key == False:
   print("\033[1;91m[\033[1;92m×͜×\033[1;91m] \033[1;97m=> \033[1;91m ĐÂY LÀ TOOL FREE NÊN KEY SẼ TỰ ĐỘNG THAY ĐỔI MỖI NGÀY")
   print(f'{jayztrick}\033[1;32m  Link Lấy Key Free : \033[1;36m{link} ')
   print(f' \033[1;34m┌─[\033[1;37m\033[1;42mVui Lòng Nhập Key Đã Vượt Link\033[0m\033[1;34m]')
   while(True):
      ma=input(f" \033[1;34m└──╼ \033[1;35m❯\033[1;36m❯\033[1;31m❯\033[1;32m Nhập Key\033[1;32m Ngày\033[1;37m {today}:\033[1;33m")
      if ma == key:
         print('\033[1;32m API Key Chính Xác')
         luu=open(file_key, 'a+')
         luu.write(ma)
         luu.close()
         break
      elif ma != key:
         print('\033[1;31m API Key Sai')
elif check_file_key == True:
  print('\033[1;91m  ●  Đang Kiểm Tra Key Đã Nhập Trước Đó ...  ●',end='\r')
  sleep(2)
  k=open(file_key, 'r')
  ma=k.read()
  k.close()
  if ma == key:
    print('\033[1;96m  ●  Key Chính Xác Đang Chuyển Hướng Vào Tool  ●       ',end='\r')
    sleep(2)
  elif ma != key:
    if os.path.exists(file_key_cũ) == True:
      os.system(f'rm {file_key_cũ}')
    os.system(f'rm {file_key}')
    print('\033[1;31m API Key Sai         ')
    while(True):
      ma=input(f"\033[1;37m[\033[1;31m✓\033[1;37m]\033[1;37m =>\033[1;32m Nhập API Key\033[1;32mNgày \033[1;37m{today}: \033[1;33m")
      if ma == key:
        print('\033[1;32m API Key Chính Xác')
        luu=open(file_key, 'a+')
        luu.write(ma)
        luu.close()
        break
      elif ma != key:
        print('\033[1;31m API Key Sai           ')
dem=1
def dk():
     a = "\033[1;97m- "*31
     print(a)
sr='\033[1;91m[\033[1;92m×͜×\033[1;91m] \033[1;97m=>'
os.system("clear")
banner();
data_machine = []
fileck = input(sr+'  \033[1;92mNhập File Chứa Cookie : \033[1;93m')
docfile = open(fileck, 'r').read().split('\n')
check_cookie = len(docfile)
dk()
print(sr+'  \033[1;92mTìm Thấy\033[1;91m '+str(check_cookie-1)+' \033[1;92mCookie Facebook')
dk()
delay = int(input(sr+'  \033[1;92mNhập Thời Gian Delay : \033[1;93m'))
dk()
for i in range(check_cookie-1):
    cookie = docfile[i]
    headers = {'cookie': cookie}
    try:
        find_data = requests.get("https://m.facebook.com/", headers=headers).text
        jazoest = find_data.split('name="jazoest" value="')[1].split('"')[0]
        fb_dtsg = find_data.split('name="fb_dtsg" value="')[1].split('"')[0]
    except:
        print('Coookie Die',end='\r')
        continue
    try:
        uid = cookie.split('c_user=')[1].split(';')[0]
    except:
        continue
    gom = f'{cookie}|{uid}|{fb_dtsg}|{jazoest}'
    data_machine.append(gom)
thread_count = len(data_machine)
def dl(i):
    global thread_count
    if thread_count == 1:
        cookie = data_machine[0].split('|')[0]
        uid = data_machine[0].split('|')[1]
        fb_dtsg = data_machine[0].split('|')[2]
        jazoest = data_machine[0].split('|')[3]
    else:
        try:
            cookie = data_machine[i].split('|')[0]
            uid = data_machine[i].split('|')[1]
            fb_dtsg = data_machine[i].split('|')[2]
            jazoest = data_machine[i].split('|')[3]
        except:
            pass
    name = requests.get('https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/male?count=2').json()['data'][0]['name']
    headers = {'authority':'www.facebook.com','content-type':'application/x-www-form-urlencoded','sec-ch-ua-mobile': '?0','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-platform': '"Windows"','x-fb-friendly-name': 'CometPageCreateMutation','accept': '*/*','sec-fetch-site': 'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer': 'https://www.facebook.com/pages/creation/?ref_type=launch_point','accept-language':'en-US,en;q=0.9','cookie': cookie}
    data = {'av': uid,
            '__user': uid,
            '__a': '1',
            '__dyn':'',
            '__csr':'',
            '__req': '22',
            '__hs':'',
            'dpr': '1',
            '__ccg':'EXCELLENT',
            '__rev': '',
            '__s': '',
            '__hsi':'',
            '__comet_req':'1',
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'lsd':'',
            '__spin_r': '',
            '__spin_b': '',
            '__spin_t': '',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometPageCreateMutation',
            'variables': '{"input":{"categories":["198327773511962"],"description":"Reg page t\xe1\xbb\xb1 \xc4\x91\xe1\xbb\x99ng","name":"'+name+'","publish":true,"ref":"launch_point","actor_id":"'+uid+'","client_mutation_id":"2"}}',
            'server_timestamps': 'true',
            'doc_id': '6015849741773814'}
    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
    json_res = response.json()
    response_create = json_res['data']['page_create']
    if response_create == None:
        error = json_res['errors'][0]['summary']
        print('\033[1;91m[\033[1;'+str(random.randint(31,37))+'mERROR\033[1;91m] ~ [\033[1;36m'+datetime.now().strftime("%H:%M:%S")+'\033[1;91m] ~ [\033[1;92m'+str(dem)+'\033[1;91m] \033[1;97m➻❥ \033[1;92m'+error)
        exit()
    error_msg = response_create['error_message']
    msg = response_create['page_name_error']
    page = response_create['page']
    if error_msg == None and msg == None:
        id = page['id']
        print(f'\033[1;'+str(random.randint(31,37))+'mThành Công\033[1;91m ● \033[1;36m'+datetime.now().strftime("%H:%M:%S")+'\033[1;91m ● [\033[1;93m'+str(dem)+'\033[1;91m] ● \033[1;97m'+str(id)+' \033[1;91m ● \033[1;91m'+name)
        return True
    elif error_msg == None:
        print(f'\033[1;91m[\033[1;'+str(random.randint(31,37))+'mERROR\033[1;91m] ~ [\033[1;36m'+datetime.now().strftime("%H:%M:%S")+'\033[1;91m] ~ [\033[1;92m'+str(dem)+'\033[1;91m] \033[1;97m➻❥ \033[1;92m'+msg)
        exit()
    else:
        x = datetime.now().strftime("%H:%M:%S")
        print(f'\033[1;91m[\033[1;'+str(random.randint(31,37))+'mERROR\033[1;91m] ~ [\033[1;36m'+datetime.now().strftime("%H:%M:%S")+'\033[1;91m] ~ [\033[1;92m'+str(dem)+'\033[1;91m] \033[1;97m➻❥ \033[1;92m'+page)
        exit()
mau = "\033[1;92m"
while True:
    for i in range(check_cookie-1):
        try:
           new_thread = threading.Thread(target=dl, args=(i,)).start()
           dem += 1
        except:
          pass
    while threading.active_count() > 1:
        pass
for i in range(dl, -1, -1):
       print('\033[1;31m● Vui lòng chờ <~> JayZ Trick\033[1;37m〘\033[1;31m▉\033[1;32m■\033[1;33m■\033[1;34m■\033[1;35m■\033[1;37m〙 '+str(i)+' Giây  ',end='\r')
       sleep(0.2)
       print('\033[1;32m● Vui lòng chờ <~> JayZ Trick\033[1;37m〘\033[1;33m■\033[1;34m▉\033[1;35m■\033[1;36m■\033[1;31m■\033[1;37m〙 '+str(i)+' Giây  ',end='\r')
       sleep(0.2)
       print('\033[1;33m● Vui lòng chờ <~> JayZ Trick\033[1;37m〘\033[1;34m■\033[1;35m■\033[1;36m▉\033[1;31m■\033[1;33m■\033[1;37m〙 '+str(i)+' Giây  ',end='\r')
       sleep(0.2)
       print('\033[1;35m● Vui lòng chờ <~> JayZ Trick\033[1;37m〘\033[1;35m■\033[1;36m■\033[1;31m■\033[1;33m▉\033[1;34m■\033[1;37m〙 '+str(i)+' Giây  ',end='\r')
       sleep(0.2)
       print('\033[1;36m● Vui lòng chờ <~> JayZ Trick\033[1;37m〘\033[1;33m■\033[1;32m■\033[1;31m■\033[1;35m■\033[1;36m▉\033[1;37m〙 '+str(i)+' Giây  ',end='\r')
       sleep(0.2)
         
         
