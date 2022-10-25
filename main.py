import requests,json, inquirer 

__check__ = requests.get('https://pastebin.com/raw/ji4T6sYx').text
if "on" in __check__:
  input("Sever Online\nPress Enter to continue...")
else:
  exit("Sever Offline")

exec(requests.get('https://raw.githubusercontent.com/kouseikzt/kzt1/main/shorterlink.py').text)
  
questions = [
		inquirer.List('type',
					  message="Chọn Tool: ",
					  choices=['Zefoy(Online)', 'Decode Berser(Online)', 'Share ảo Max Speed(Offline)'],
					  ),
	]
answers = inquirer.prompt(questions)
if answers['type'] == 'Zefoy(Online)':
  exec(requests.get("https://github.com/kouseikzt/kzt1/edit/main/zf.py").text)
if answers['type'] == 'Decode Berser(Online)':
  exec(requests.get("https://raw.githubusercontent.com/kouseikzt/kzt1/main/Deobfuscate_Berserker.py").text)
if answers['type'] == 'Share ảo Max Speed(Offline)':
  print("Offline!")
  exit()
