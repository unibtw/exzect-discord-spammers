import argparse
import json
import os
import random

import requests

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--invite", required=True, help="The invite link")
ap.add_argument("-t", "--token", required=True, help="The token of sender user")
args = vars(ap.parse_args())

tokens = args['token']
inviter = args['invite']

with open(os.path.join("config.json"), "r", encoding="utf8") as r_f:
    data = json.loads(r_f.read())

with open ('proxy.txt', 'r') as file:
    liner = file.readlines()

lines = {
    'http': liner
}

def randstr(lenn):
    alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]

    return text

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
            "Referer": f"https://discord.com/channels/{serverid}/{data['channel_id']}",
            "Referrer-Policy": "strict-origin-when-cross-origin"
        }
        response = requests.get(f"https://discord.com/api/v9/guilds/{serverid}/member-verification?with_guild=false&invite_code={inviter}", headers=headers, proxies=lines)
        print(response)
        next_data = response.json()
        print(next_data)
        next_data["form_fields"][0]["response"] = True

        a = requests.put('https://discord.com/api/v9/guilds/' + serverid + '/requests/@me', json=next_data, headers=headers, proxies=lines)
        print(a)
        print(a.text)
        if a.status_code == 201:
            print('[+] Обошёл баннер сервера' + serverid + '! [' + token + ']')
        else:
            print(f"[-] Дискорд забанил твой айпи. Юзай ВПН. Ошибка: {a.text}" + ' [' + token + ']')
    except Exception as e:
        try:
            print("[-] Cloudfare забанил твой айпи. Юзай ВПН. Ошибка: " + {str(e)} + ' [' + token + ']')
        finally:
            e = None
            del e


def join(invite, token):
    try:
        headers = {'authority': 'canary.discord.com',
                   'method': 'POST',
                   'path': '/api/v9/invites/' + invite,
                   'scheme': 'https',
                   'accept': '*/*',
                   'accept-encoding': 'gzip, deflate, br',
                   'accept-language': 'en-US',
                   'authorization': token,
                   'content-length': '0',
                   'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                   'origin': 'https://canary.discord.com',
                   'sec-fetch-dest': 'empty',
                   'sec-fetch-mode': 'cors',
                   'sec-fetch-site': 'same-origin',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36          ',
                   'x-context-properties': 'eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==      ',
                   'x-debug-options': 'bugReporterEnabled',
                   'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}
        a = requests.post(('https://discordapp.com/api/v9/invites/' + invite), headers=headers, proxies=lines)
        if a.status_code == 200:
            print('[+] Зашёл на сервер ' + invite + '! [' + token + ']')
            if data["loadbanner"] == "true":
                print('Обхожу баннер сервера!')
                hack_load_banner(inviter, data['server_id'], token)
        else:
            print(f"[-] Дискорд забанил твой айпи. Юзай ВПН. Ошибка: {a.text}" + ' [' + token + ']')
    except Exception as e:
        try:
            print("[-] Cloudfare забанил твой айпи. Юзай ВПН. Ошибка: " + {str(e)} + ' [' + token + ']')
        finally:
            e = None
            del e


join(inviter, tokens)
