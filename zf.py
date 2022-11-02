import os
import datetime
import random
import time
import inquirer
from colorama import init, Fore
from prettytable import PrettyTable
import re
import base64
import requests
import urllib.parse
from bs4 import BeautifulSoup
from urllib.parse import urlparse


# for debug
# from requests_toolbelt.utils import dump


class ZefoyViews:
	API_ZEFOY = 'https://zefoy.com/'
	API_VISION = 'https://api.sandroputraa.com/zefoy.php'

	STATIC_HEADERS = {
		"origin": "https://zefoy.com",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
		"x-requested-with": "XMLHttpRequest",
		'Host': 'zefoy.com',

	}

	STATIC_ENDPOINT = {
		"Views": "c2VuZC9mb2xsb3dlcnNfdGlrdG9V",
		"Shares": "c2VuZC9mb2xsb3dlcnNfdGlrdG9s",
		"Favorites": "c2VuZF9mb2xsb3dlcnNfdGlrdG9L",
		"Hearts": "c2VuZE9nb2xsb3dlcnNfdGlrdG9r"
	}

	def __init__(self):
		self.key_views = None
		self.session = requests.Session()
		self.captcha = None
		self.phpsessid = None

	def captcha_solver(self):
		solve_captcha = requests.post(
			url=self.API_VISION,
			headers={
				'Content-Type': 'application/json',
				'Auth': 'sandrocods',
				'Host': 'api.sandroputraa.com',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
			},
			json={
				"img": base64.b64encode(open('captcha.png', 'rb').read()).decode('utf-8')
			}
		)
		if solve_captcha.status_code == 200 and solve_captcha.json()['Message'] == 'Success':
			return solve_captcha.json()['Data']
		else:
			exit("Error: " + solve_captcha.json()['message'])

	def get_session_captcha(self):
		request_session = self.session.get(
			url=self.API_ZEFOY,
			headers=self.STATIC_HEADERS,
		)

		soup = BeautifulSoup(request_session.text, 'html.parser')

		# Download Captcha Image
		try:

			request_captcha_image = self.session.get(
				url=self.API_ZEFOY + soup.find('img', {'alt': 'CAPTCHA code'}).get('src'),
				headers=self.STATIC_HEADERS,
			)

			with open('captcha.png', 'wb') as f:
				f.write(request_captcha_image.content)

			self.phpsessid = request_session.cookies.get_dict()['PHPSESSID']
		except AttributeError:
			self.get_session_captcha()

	def post_solve_captcha(self, captcha_result):

		try:
			self.STATIC_HEADERS['cookie'] = "PHPSESSID=" + self.phpsessid
			self.STATIC_HEADERS['content-type'] = "application/x-www-form-urlencoded; charset=UTF-8"

			post_captcha = self.session.post(
				url=self.API_ZEFOY,
				headers=self.STATIC_HEADERS,
				data={
					'captcha_secure': captcha_result,
					'r75619cf53f5a5d7aa6af82edfec3bf0': '',
				}
			)
			soup = BeautifulSoup(post_captcha.text, 'html.parser')
			self.key_views = soup.find('input', {'placeholder': 'Enter Video URL'}).get('name')
			return True
		except Exception as e:
			return "Error: " + str(e)

	def get_status_services(self):
		try:
			temp_status = []
			self.STATIC_HEADERS['cookie'] = "PHPSESSID=" + self.phpsessid
			self.STATIC_HEADERS['content-type'] = "application/x-www-form-urlencoded; charset=UTF-8"

			get_status_services = self.session.get(
				url=self.API_ZEFOY,
				headers=self.STATIC_HEADERS,
			)
			soup = BeautifulSoup(get_status_services.text, 'html.parser')
			for i in soup.find_all('div', {'class': 'col-sm-4 col-xs-12 p-1 colsmenu'}):
				temp_status.append({
					'name': i.findNext('h5').text.strip(),
					'status': i.findNext('small').text.strip()
				})
			return temp_status
		except Exception:
			self.get_status_services()

	def send_multi_services(self, url_video, services):
		global soup
		try:
			self.STATIC_HEADERS['cookie'] = "PHPSESSID=" + self.phpsessid
			self.STATIC_HEADERS['content-type'] = "application/x-www-form-urlencoded; charset=UTF-8"

			post_services = self.session.post(
				url=self.API_ZEFOY + self.STATIC_ENDPOINT[services],
				headers=self.STATIC_HEADERS,
				data={
					self.key_views: url_video,
				}
			)

			decode_old = base64.b64decode(urllib.parse.unquote(post_services.text[::-1])).decode()
			soup = BeautifulSoup(decode_old, 'html.parser')

			if "An error occurred. Please try again." in decode_old:

				decode = self.force_send_multi_services(
					url_video=url_video,
					old_request=decode_old,
					services=services
				)

				if "Successfully " + services.lower() + " sent." in decode:
					return {
						'message': 'Successfully ' + services.lower() + ' sent.',
						'data': soup.find('button').text.strip()
					}
				else:
					return {
						'message': 'Another State',
						'data': soup.find('button').text.strip()
					}

			elif "Successfully " + services.lower() + " sent." in decode_old:
				return {
					'message': 'Successfully ' + services.lower() + ' sent.',
					'data': soup.find('button').text.strip()
				}

			elif "Session Expired. Please Re Login!" in decode_old:
				return {
					'message': 'Please try again later. Server too busy.',
				}

			# Getting Timer
			try:

				return {
					'message': re.search(r"var ltm=[0-9]+;", decode_old).group(0).replace("ltm=", "") \
						.replace(";", "").replace("var", "").strip()
				}
			except:
				pass

		except Exception as e:

			return "Error: " + str(e)

	def force_send_multi_services(self, url_video, services, old_request):

		if 'tiktok' in url_video:
			if len(urlparse(url_video).path.split('/')[-1]) == 19:
				valid_id = urlparse(url_video).path.split('/')[-1]
			else:
				return False
		else:
			return False

		parse = BeautifulSoup(old_request, 'html.parser')

		self.STATIC_HEADERS['cookie'] = "PHPSESSID=" + self.phpsessid
		request_force_multiple_services = self.session.post(
			url=self.API_ZEFOY + self.STATIC_ENDPOINT[services],
			headers=self.STATIC_HEADERS,
			data={
				parse.find('input', {'type': 'text'}).get('name'): valid_id,
			}
		)
		decode = base64.b64decode(urllib.parse.unquote(request_force_multiple_services.text[::-1])).decode()
		return decode


def main():
	os.system("cls" if os.name == "nt" else "clear"); os.system("title TikTok Zefoy by @HuyKazuto" if os.name == "nt" else "")
	init(autoreset=True)
	inject = ZefoyViews()
	print(
		Fore.GREEN + """
			░█─░█ █──█ █──█ ░█─▄▀ █▀▀█ ▀▀█ █──█ ▀▀█▀▀ █▀▀█ 
			░█▀▀█ █──█ █▄▄█ ░█▀▄─ █▄▄█ ▄▀─ █──█ ──█── █──█ 
			░█─░█ ─▀▀▀ ▄▄▄█ ░█─░█ ▀──▀ ▀▀▀ ─▀▀▀ ──▀── ▀▀▀▀

													
							▀█ █▀█ █▀█ █▀█
							█▄ █▄█ █▄█ ▀▀█
	"""
	)
	print(Fore.LIGHTYELLOW_EX + "Example: https://www.tiktok.com/@huykazuto9/video/7092669682594876699")
	url_video = input("Enter URL Video: ")
	date = datetime.datetime.now()
	hours = date.strftime("%H:%M:%S")
	inject.get_session_captcha()
	time.sleep(1)

	if inject.post_solve_captcha(captcha_result=inject.captcha_solver()):

		print("\n[ " + str(hours) + " ] " + Fore.LIGHTGREEN_EX + "Success Solve Captcha" + "\n")

		table = PrettyTable(field_names=["Services", "Status"], title="Status Services", header_style="upper",
							border=True)
		status_services = inject.get_status_services()
		if status_services is None: print("Failed to get status services, try again later"); exit()

		valid_services = []
		for service in status_services:
			if service['name'] == 'Followers' or service['name'] == 'Comments Hearts':
				continue
			elif 'ago updated' in service['status']:
				valid_services.append(service['name'])

			table.add_row([service['name'], Fore.GREEN + service['status'] + Fore.RESET if 'ago updated' in service[
				'status'] else Fore.RED + service['status'] + Fore.RESET])

		table.title = Fore.YELLOW + " Total Online Services: " + str(len(valid_services)) + Fore.RESET
		print(table)

		questions = [
			inquirer.List('type', message="What services do you need?", choices=valid_services, carousel=True, ), ]
		answers = inquirer.prompt(questions)

		while True:

			try:

				if answers['type'] == 'Views':
					os.system("cls" if os.name == "nt" else "clear"); os.system("title TikTok Viewbot by @HuyKazuto" if os.name == "nt" else "")
					while True:
						inject_views = inject.send_multi_services(url_video=url_video, services=answers['type'], )

						if inject_views:

							if inject_views['message'] == "Please try again later":
								print("[ " + str(hours) + " ] " + Fore.LIGHTRED_EX + inject_views[
									'message'])
								exit()

							elif inject_views['message'] == 'Another State':
								print("[ " + str(
									hours) + " ] " + Fore.LIGHTGREEN_EX + "Current Views: " +
									  inject_views['data'], end="\r")


							elif inject_views['message'] == "Successfully views sent.":
								print("[ " + str(hours) + " ] " + Fore.LIGHTGREEN_EX + inject_views[
									'message'] + " to " + Fore.LIGHTYELLOW_EX + "" + url_video + ", " + Fore.LIGHTGREEN_EX + "Current Views: " +
									  inject_views['data'], end="\n\n")
								print()

							elif inject_views['message'] == "Session Expired. Please Re Login!":
								print("[ " + str(hours) + " ] " + Fore.LIGHTRED_EX + inject_views[
									'message'])
								exit()



							else:
								for i in range(int(inject_views['message']), 0, -1):
									print("[ " + str(
										hours) + " ] " + Fore.LIGHTYELLOW_EX + "Please wait " + str(
										i) + " seconds to send views again.", end="\r")
									time.sleep(1)

							time.sleep(random.randint(1, 5))

						else:
							pass

				elif answers['type'] == 'Shares':
					os.system("cls" if os.name == "nt" else "clear"); os.system("title TikTok Sharebot by @HuyKazuto" if os.name == "nt" else "")
					while True:
						inject_shares = inject.send_multi_services(url_video=url_video, services=answers['type'], )

						if inject_shares:

							if inject_shares['message'] == "Please try again later":
								print("[ " + str(hours) + " ] " + Fore.LIGHTRED_EX + inject_shares[
									'message'])
								exit()

							elif inject_shares['message'] == 'Another State':
								print("[ " + str(
									hours) + " ] " + Fore.LIGHTGREEN_EX + "Current Shares : " +
									  inject_shares['data'], end="\n\n")
								print()


							elif inject_shares['message'] == "Shares successfully sent.":
								print("[ " + str(hours) + " ] " + Fore.LIGHTGREEN_EX + inject_shares[
									'message'] + " to " + Fore.LIGHTYELLOW_EX + "" + Fore.LIGHTGREEN_EX + "Current Shares: " +
									  inject_shares['data'], end="\r")


							elif inject_shares['message'] == "Session Expired. Please Re Login!":
								print("[ " + str(hours) + " ] " + Fore.LIGHTRED_EX + inject_shares[
									'message'])
								exit()


							else:
								for i in range(int(inject_shares['message']), 0, -1):
									print("[ " + str(
										hours) + " ] " + Fore.LIGHTYELLOW_EX + "Please wait " + str(
										i) + " seconds to send Shares again.", end="\r")
									time.sleep(1)

							time.sleep(random.randint(1, 5))

						else:
							pass

				elif answers['type'] == 'Favorites':
					os.system("cls" if os.name == "nt" else "clear"); os.system("title TikTok Favoritebot by @HuyKazuto" if os.name == "nt" else "")
					while True:
						inject_favorites = inject.send_multi_services(url_video=url_video, services=answers['type'], )

						if inject_favorites:

							if inject_favorites['message'] == "Please try again later":
								print("[ " + str(hours) + " ] " + Fore.LIGHTRED_EX + inject_favorites[
									'message'])
								exit()

							elif inject_favorites['message'] == 'Another State':
								print("[ " + str(
									hours) + " ] " + Fore.LIGHTGREEN_EX + "Current Favorites : " +
									  inject_favorites['data'], end="\r")


							elif inject_favorites['message'] == "Favorites successfully sent.":
								print(
									"[ " + str(hours) + " ] " + Fore.LIGHTGREEN_EX + inject_favorites[
										'message'] + " to " + Fore.LIGHTYELLOW_EX + "" + url_video + Fore.LIGHTGREEN_EX + "Current Favorites : " +
									inject_favorites['data'], end="\n\n")
								print()

							elif inject_favorites['message'] == "Session Expired. Please Re Login!":
								print("[ " + str(hours) + " ] " + Fore.LIGHTRED_EX + inject_favorites[
									'message'])
								exit()



							else:
								for i in range(int(inject_favorites['message']), 0, -1):
									print("[ " + str(
										hours) + " ] " + Fore.LIGHTYELLOW_EX + "Please wait " + str(
										i) + " seconds to send Favorites again.", end="\r")
									time.sleep(1)

							time.sleep(random.randint(1, 5))

						else:
							pass

				elif answers['type'] == 'Hearts':
					os.system("cls" if os.name == "nt" else "clear"); os.system("title TikTok Heartbot by @HuyKazuto" if os.name == "nt" else "")
					while True:
						inject_hearts = inject.send_multi_services(url_video=url_video, services=answers['type'], )

						if inject_hearts:

							if inject_hearts['message'] == "Please try again later":
								print("[ " + str(hours) + " ] " + Fore.LIGHTRED_EX + inject_hearts[
									'message'])
								exit()

							elif inject_hearts['message'] == 'Another State':
								print("[ " + str(
									hours) + " ] " + Fore.LIGHTGREEN_EX + "Current Hearts : " +
									  inject_hearts['data'], end="\r")


							elif inject_hearts['message'] == "Hearts successfully sent.":
								print("[ " + str(hours) + " ] " + Fore.LIGHTGREEN_EX + inject_hearts[
									'message'] + " to " + Fore.LIGHTYELLOW_EX + "" + url_video + Fore.LIGHTGREEN_EX + "Current Hearts: " +
									  inject_hearts['data'], end="\n\n")
								print()

							elif inject_hearts['message'] == "Session Expired. Please Re Login!":
								print("[ " + str(hours) + " ] " + Fore.LIGHTRED_EX + inject_hearts[
									'message'])
								exit()



							else:
								for i in range(int(inject_hearts['message']), 0, -1):
									print("[ " + str(
										hours) + " ] " + Fore.LIGHTYELLOW_EX + "Please wait " + str(
										i) + " seconds to send Hearts again.", end="\r")
									time.sleep(1)

							time.sleep(random.randint(1, 5))

						else:
							pass

			except Exception as e:
				print(
					"[ " + str(hours) + " ] " + Fore.LIGHTRED_EX + "Unpredictable error : " + str(e))

	else:
		print(Fore.RED + "Failed to solve captcha.")


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print(Fore.RED + "Exit")
		exit()
