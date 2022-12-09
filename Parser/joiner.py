import argparse
import json
import os
import random
from capmonster_python import HCaptchaTask
import requests

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--invite", required=True, help="The invite link")
ap.add_argument("-t", "--token", required=True, help="The token of sender user")
args = vars(ap.parse_args())

tokens = args['token']
invite_code = args['invite']

headers = {
	"x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjkzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTMuMCIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAwODA0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
	"sec-fetch-dest": "empty",
	"x-debug-options": "bugReporterEnabled",
	"sec-fetch-mode": "cors",
	"sec-fetch-site": "same-origin",
	"accept": "*/*",
	"accept-language": "en-GB",
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

with open ('proxy.txt', 'r') as file:
    lines = file.readlines()
    proxer = random.choice(lines)

proxies = {
    'http': proxer
}

with open(os.path.join("config.json"), "r", encoding="utf8") as r_f:
    data = json.loads(r_f.read())


def randstr(lenn):
    alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]

    return text

def request_cookie():
	response1 = requests.get("https://discord.com")
	cookie = response1.cookies.get_dict()
	cookie['locale'] = "us"
	return cookie

def request_fingerprint():
	response2 = requests.get("https://discordapp.com/api/v9/experiments", headers=headers_reg).json()
	fingerprint = response2["fingerprint"]
	return fingerprint

def captcha_bypass(url, key):
	if data['captcha_type'] == "capmonster":
		capmonster = HCaptchaTask(data["capmonster_apikey"])
		task_id = capmonster.create_task(url, key)
		result = capmonster.join_task_result(task_id)
		response = result.get("gRecaptchaResponse")
		print(f"[+] Captcha решена ({response[-32:]})")
		return response    


# def hack_load_banner(inviter, serverid, token):
#     try:
#         headers = {
#             "accept": "*/*",
#             "accept-language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
#             "authorization": f"{token}",
#             "content-type": "application/json",
#             "sec-ch-ua": "\"Microsoft Edge\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
#             "sec-ch-ua-mobile": "?1",
#             "sec-ch-ua-platform": "\"Android\"",
#             "sec-fetch-dest": "empty",
#             "sec-fetch-mode": "cors",
#             "sec-fetch-site": "same-origin",
#             "x-debug-options": "bugReporterEnabled",
#             "x-discord-locale": "ru",
#             "x-kl-ajax-request": "Ajax_Request",
#             "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InJ1IiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMDcuMC4xNDE4LjYyIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE2MjIxNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
#             "cookie": "__dcfduid=912182c06a6f11ed8191edf22d8a6ff8; __sdcfduid=912182c16a6f11ed8191edf22d8a6ff877f0cc11099fff8ed872ee4e83dba09ac19fa480998a78f11c8723b3c44d66ec; _ga=GA1.2.494028496.1669126585; _gcl_au=1.1.372643739.1670056080; _gid=GA1.2.1059993064.1670056083; locale=ru; __cfruid=815c1c8aadffc710574c266db82b2fa46d863842-1670057560; OptanonConsent=isIABGlobal=false&datestamp=Sat+Dec+03+2022+13%3A52%3A42+GMT%2B0500+(%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __cf_bm=pj5x1ApKkQa39ywbrcyVclVtvPLOUsNPIdHzz2EBhIw-1670057561-0-AWJ5yqUXtFcqpeXLegJTn6f2hsOMI4e3geBCm47b6HjpyR1P8WVbxN3/BzahSpnAgdwbUKQC6B9Y0dYm/Xp32HE=",
#             "Referer": f"https://discord.com/channels/{serverid}/{data['channel_id']}",
#             "Referrer-Policy": "strict-origin-when-cross-origin"
#         }
#         response = requests.get(f"https://discord.com/api/v9/guilds/{serverid}/member-verification?with_guild=false&invite_code={inviter}", headers=headers)
#         next_data = response.json()
#         a = requests.put('https://discord.com/api/v9/guilds/' + serverid + '/requests/@me', json=next_data, headers=headers)
#         if a.status_code == 201:
#             print('[+] Обошёл баннер сервера' + serverid + '! [' + token + ']')
#         else:
#             print(f"[-] Дискорд забанил твой айпи. Юзай ВПН. Ошибка: {a.text}" + ' [' + token + ']')
#     except Exception as e:
#         try:
#             print("[-] Cloudfare забанил твой айпи. Юзай ВПН. Ошибка: " + {str(e)} + ' [' + token + ']')
#         finally:
#             e = None
#             del e


def join(invite_code, token):
		headers["authorization"] = token
		headers["x-fingerprint"] = request_fingerprint()
		response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headers, cookies=request_cookie(), proxies=proxies, timeout=20)
		if response.status_code == 400:
			print(f"[!] Captcha {token[:50]}****** обнаружена! Решаю.. ({response.json()['captcha_sitekey']})")
			response_captcha = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", json={"captcha_key": captcha_bypass("https://discord.com", f"{response.json()['captcha_sitekey']}")}, headers=headers, cookies=request_cookie(), proxies=proxies, timeout=20)
			if response_captcha.status_code == 200:
				print(f"[+] {token[:50]}****** зашёл на сервер! ({invite_code})")
				body = response_captcha.json()
				guild_id = body['guild']['id']
				if 'show_verification_form' in body:
					get_rules = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false", headers=headers, cookies=request_cookie(), proxies=proxies, timeout=20).json()
					response2 = requests.put(f"https://discord.com/api/v9/guilds/{guild_id}/requests/@me", headers=headers, cookies=request_cookie(), json=get_rules, proxies=proxies, timeout=20)
					if response2.status_code == 201 or response2.status_code == 204:
						print(f"[+] {token[:50]}****** принял правила сервера!")
					else:
						print(f"[!] {token[:50]}****** не принял правила сервера! ({response2.content})")

		elif response.status_code == 200:
			print(f"[+] {token[:50]}****** зашёл на сервер! ({invite_code})")
			body = response.json()
			guild_id = body['guild']['id']
			if 'show_verification_form' in body:
				get_rules = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false", headers=headers, cookies=request_cookie(), proxies=proxies, timeout=20).json()
				response2 = requests.put(f"https://discord.com/api/v9/guilds/{guild_id}/requests/@me", headers=headers, cookies=request_cookie(), json=get_rules, proxies=proxies, timeout=20)
				if response2.status_code == 201 or response2.status_code == 204:
					print(f"[+] {token[:50]}****** принял правила сервера!")
				else:
					print(f"[!] {token[:50]}****** не принял правила сервера! ({response2.content})")
		else:
			print(f"[!] {token[:50]}****** не зашёл на сервер! ({response.content})")


join(invite_code, tokens)
