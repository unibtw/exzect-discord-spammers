import discum
import argparse 
import time
import json as js
import os 
import re
import random
import requests
import datetime
from capmonster_python import HCaptchaTask
import discord

with open(os.path.join("config.json"), "r", encoding="utf8") as r_f:
			data = js.loads(r_f.read())

ap = argparse.ArgumentParser()
ap.add_argument("-id", "--indeficator", required=True, help="The id of user")
ap.add_argument("-t", "--token", required=True, help="The token of sender user")

args = vars(ap.parse_args())

tokener = args["token"]
idder = args["indeficator"]

with open("text.txt", "r", encoding="utf8") as r_f:
	text_to_send = r_f.read()

with open ('proxy.txt', 'r') as file:
    lines = file.readlines()
    proxer = random.choice(lines)

proxyip = proxer.split(":")[0]
proxyport = proxer.split(":")[1]
liner = {
    'http': lines
}

headers = {
		"x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjkzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTMuMCIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAwODA0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
		"sec-fetch-dest": "empty",
		"x-debug-options": "bugReporterEnabled",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-origin",
		"accept": "*/*",
		"accept-language": "en-GB",
		"content-type": "application/json",
		"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.16 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
		"TE": "trailers"
	}

headers_reg = {
	    "accept": "*/*",
	    "authority": "discord.com",
	    "method": "POST",
	    "path": "/api/v9/auth/register",
	    "scheme": "https",
	    "origin": "discord.com",
	    "referer": "discord.com/register",
	    "x-debug-options": "bugReporterEnabled",
	    "accept-language": "en-US,en;q=0.9",
	    "connection": "keep-alive",
	    "content-Type": "application/json",
	    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
	    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
	    "sec-fetch-dest": "empty",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-site": "same-origin"
	}

def request_cookie():
	response1 = requests.get("https://discord.com", proxies=liner)
	cookie = response1.cookies.get_dict()
	cookie['locale'] = "us"
	return cookie

with open('Users.txt') as fp:
	userss = fp.readlines()

def request_fingerprint():
	response2 = requests.get("https://discordapp.com/api/v9/experiments", headers=headers_reg, proxies=liner).json()
	fingerprint = response2["fingerprint"]
	return fingerprint

def open_channel(authorization, userID):
	json_data = {'recipient_id': userID}
	headers['x-fingerprint'] = request_fingerprint()
	headers['authorization'] = authorization
	headers['x-context-properties'] = "e30="
	response3 = requests.post("https://discord.com/api/v9/users/@me/channels", headers=headers, cookies=request_cookie(), json=json_data, proxies=liner).json()
	channel = response3["id"]
	return channel

def request_snowflake():
	snakeflow = discord.utils.time_snowflake(datetime.datetime.now())
# datetime_obj=
	return snakeflow	

def captcha_bypass(token, url, key, captcha_rqdata):
	capmonster = HCaptchaTask(data['capmonster_apikey'])
	capmonster.set_user_agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.16 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36")
	task_id = capmonster.create_task(url, key, is_invisible=True, custom_data=captcha_rqdata)
	result = capmonster.join_task_result(task_id)
	response = result.get("gRecaptchaResponse")
	dateTimeObj = datetime.datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M:%S")
	print(f"[{timestampStr}] [CAPTCHA SOLVED] ({response[-32:]}) ({token[:36]}*****)")
	return response	

channel = open_channel(tokener, idder)
# bot = discum.Client(token=args["token"], proxy_host=proxyip, proxy_port=proxyport)
pattern = re.compile(re.escape(args["indeficator"]))	
# print('Сплю ' +str(data["timeout"])+' секунд')
# time.sleep(int(data["timeout"]))
# bot.sendMessage(channel, text_to_send)
# bot.sendFile(newDM,"https://media.discordapp.net/attachments/1048927238315323476/1048927705061658634/image.png?width=1193&height=671",True)

def send_message(authorization, channel, msg, userID):
	dateTimeObj = datetime.datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M:%S")
	snakeflow = request_snowflake()
	jsoner = {'content': msg, 'nonce': snakeflow, 'tts': "false"}
	headers['x-fingerprint'] = request_fingerprint()
	headers['authorization'] = authorization
	headers['referer'] = "https://discord.com/channels/@me/" + str(channel)
	response4 = requests.post("https://discord.com/api/v9/channels/" + str(channel) + "/messages", headers=headers, cookies=request_cookie(), data=js.dumps(jsoner).replace("<user>", f"<@{userID}>").replace("<id>", f"{userID}"), proxies=liner, timeout=20)
	if response4.status_code == 200:
		print(f'Успешно {userID} ({authorization[:36]}*****)')
	elif response4.status_code == 403:
		print(f'ЛС Закрыт {userID} ({authorization[:36]}*****)')
	elif response4.status_code == 400:
		print(f"[CAPTCHA] ({authorization[:36]}*****)")
		json2 = {'captcha_key': captcha_bypass(authorization, "https://discord.com", f"{response4.json()['captcha_sitekey']}", response4.json()['captcha_rqdata']), 'captcha_rqtoken': response4.json()['captcha_rqtoken'], 'content': msg["content"], 'nonce': snakeflow, 'tts': "false"}
		response5 = requests.post("https://discord.com/api/v9/channels/" + str(channel) + "/messages", headers=headers, cookies=request_cookie(), data=js.dumps(json2).replace("<user>", f"<@{userID}>").replace("<id>", f"{userID}"), proxies=liner, timeout=20)
		if response5.status_code == 200:
			print(f'Успешно {userID} ({authorization[:36]}*****)')
		elif response5.status_code == 403:
			print(f'ЛС Закрыт {userID} ({authorization[:36]}*****)')
		else:
			print(f"[{timestampStr}] [ERROR] {userID} ({authorization[:36]}*****) ({response5.text})")

	else:
		print(f"[{timestampStr}] [ERROR] {userID} ({authorization[:36]}*****) ({response4.text})")

send_message(tokener, channel, text_to_send, idder)		

with open('Users.txt', 'w') as f:
	for line in userss:
		result = pattern.search(line)
		if result is None:
			f.write(line) 