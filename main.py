import requests,json, inquirer 

__check__ = requests.get('https://raw.githubusercontent.com/huykazuto/sever/main/Sever.txt').text
if "on" in __check__:
  exit("Sever Offline...")
else:
  exit("Sever Offline")

exec(requests.get('https://raw.githubusercontent.com/kouseikzt/kzt1/main/shorterlink.py').text)
  
questions = [
		inquirer.List('type',
					  message="Chọn Tool: ",
					  choices=['Zefoy(Online)', 'Decode Berser(Online)', 'Share ảo Max Speed(Online)'],
					  ),
	]
answers = inquirer.prompt(questions)
if answers['type'] == 'Zefoy(Online)':
	exec(requests.get("https://raw.githubusercontent.com/kouseikzt/kzt1/main/zf.py").text)
if answers['type'] == 'Decode Berser(Online)':
	exec(requests.get("https://raw.githubusercontent.com/kouseikzt/kzt1/main/Deobfuscate_Berserker.py").text)
if answers['type'] == 'Share ảo Max Speed(Online)':
	input("Lưu ý: Dán token vào file r enter 1 dòng. Đọc xog r thì enter để continue=)))")
	exec(requests.get('https://raw.githubusercontent.com/kouseikzt/kzt1/main/Shao.py').text)
  
