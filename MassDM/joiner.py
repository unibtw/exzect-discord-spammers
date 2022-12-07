import argparse
import json as js
import os
import random
import discord, datetime
import requests
from capmonster_python import HCaptchaTask

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--invite", required=True, help="The invite link")
ap.add_argument("-t", "--token", required=True, help="The token of sender user")
args = vars(ap.parse_args())

tokens = args['token']
inviter = args['invite']

with open(os.path.join("config.json"), "r", encoding="utf8") as r_f:
    data = js.loads(r_f.read())

with open('proxy.txt', 'r') as file:
    liner = file.readlines()
    proxer = random.choice(liner)

lines = {
    'http': proxer
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

def randstr(lenn):
    alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]

    return text

def request_cookie():
	response1 = requests.get("https://discord.com", proxies=lines)
	cookie = response1.cookies.get_dict()
	cookie['locale'] = "us"
	return cookie

def request_fingerprint():
	response2 = requests.get("https://discordapp.com/api/v9/experiments", headers=headers_reg, proxies=lines).json()
	fingerprint = response2["fingerprint"]
	return fingerprint    

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

def hack_load_banner(inviter, serverid, token):
    try:
        headers = {
            "accept": "*/*",
            "accept-language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
            "authorization": f"{token}",
            "content-type": "application/json",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "ru",
            "x-kl-ajax-request": "Ajax_Request",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InJ1IiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMDcuMC4xNDE4LjYyIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE2MjIxNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
            "cookie": "__dcfduid=912182c06a6f11ed8191edf22d8a6ff8; __sdcfduid=912182c16a6f11ed8191edf22d8a6ff877f0cc11099fff8ed872ee4e83dba09ac19fa480998a78f11c8723b3c44d66ec; _ga=GA1.2.494028496.1669126585; _gcl_au=1.1.372643739.1670056080; _gid=GA1.2.1059993064.1670056083; locale=ru; __cfruid=815c1c8aadffc710574c266db82b2fa46d863842-1670057560; OptanonConsent=isIABGlobal=false&datestamp=Sat+Dec+03+2022+13%3A52%3A42+GMT%2B0500+(%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __cf_bm=pj5x1ApKkQa39ywbrcyVclVtvPLOUsNPIdHzz2EBhIw-1670057561-0-AWJ5yqUXtFcqpeXLegJTn6f2hsOMI4e3geBCm47b6HjpyR1P8WVbxN3/BzahSpnAgdwbUKQC6B9Y0dYm/Xp32HE=",
            "Referer": f"",
            "Referrer-Policy": "strict-origin-when-cross-origin"
        }
        response = requests.get(f"https://discord.com/api/v9/guilds/{serverid}/member-verification?with_guild=false&invite_code={inviter}", headers=headers, proxies=lines)
        next_data = response.json()
        # next_data["form_fields"][0]["response"] = True
        a = requests.put('https://discord.com/api/v9/guilds/' + serverid + '/requests/@me', json=next_data, headers=headers, proxies=lines)
        if a.status_code == 201:
            print('[+] Обошёл баннер сервера ' + serverid + '! [' + token[:36] + '*****]')
        else:
            print(f"[-] Дискорд забанил твой айпи. Юзай ВПН. Ошибка: {a.text}" + ' [' + token[:36] + '*****]')
    except Exception as e:
        try:
            print("[-] Cloudfare забанил твой айпи. Юзай ВПН. Ошибка: " + {str(e)} + ' [' + token[:36] + '*****]')
        finally:
            e = None
            del e


def join(invite, token):
    try:
        snakeflow = request_snowflake()
        headers['x-fingerprint'] = request_fingerprint()
        jsoner = {'nonce': snakeflow, 'tts': "false"}
        headers['authorization'] = token
        headers['referer'] = "https://discordapp.com/api/v9/invites/" + str(invite)
        response4 = requests.post(('https://discordapp.com/api/v9/invites/' + invite), headers=headers, json=js.dumps(jsoner), cookies=request_cookie(), proxies=lines)
        if response4.status_code == 200:
            print('[+] Зашёл на сервер ' + invite + '! [' + token[:36] + '*****]')
            if data["loadbanner"] == "true":
                print('Обхожу баннер сервера!')
                hack_load_banner(inviter, data['server_id'], token)
        elif response4.status_code == 403:
            print(f'Ошибка 403 ({token[:36]}*****)')
        elif response4.status_code == 400:
            print(f"[CAPTCHA] ({token[:36]}*****)")
            print(response4.text)
            #json2 = {'captcha_key': captcha_bypass(token, "https://discord.com", f"{response4.json()['captcha_sitekey']}"), 'nonce': snakeflow, 'tts': "false"}
            json2 = {'captcha_key': captcha_bypass(token, "https://discord.com", f"{response4.json()['captcha_sitekey']}", response4.json()['captcha_rqdata']), 'captcha_rqtoken': response4.json()['captcha_rqtoken'], 'nonce': snakeflow, 'tts': "false"}
            response5 = requests.post("https://discordapp.com/api/v9/invites/" + str(invite), headers=headers, cookies=request_cookie(), json=js.dumps(json2), proxies=lines, timeout=20)
            if response5.status_code == 200:
                print(f'Успешно ({token[:36]}*****)')
                if data["loadbanner"] == "true":
                    print('Обхожу баннер сервера!')
                    hack_load_banner(inviter, data['server_id'], token)
                elif response5.status_code == 403:
                    print(f'Ошибка 403 ({token[:36]}*****)')
        else:
            print(f"[ERROR] ({token[:36]}*****) ({response5.text})")
    except Exception as e:    
        try:
            print("[-] Cloudfare забанил твой айпи. Юзай ВПН. Ошибка: " + {str(e)} + ' [' + token + ']')
        finally:
            e = None
            del e



join(inviter, tokens)
