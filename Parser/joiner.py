import requests
import argparse 
import random

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--invite", required=True, help="The invite link")
ap.add_argument("-t", "--token", required=True, help="The token of sender user")
args = vars(ap.parse_args())

tokens = args['token']
inviter = args['invite']

def randstr(lenn):
    alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]

    return text

def join(invite, token):
    try:
        headers = {'authority':'canary.discord.com', 
             'method':'POST', 
             'path':'/api/v9/invites/' + invite, 
             'scheme':'https', 
             'accept':'*/*', 
             'accept-encoding':'gzip, deflate, br', 
             'accept-language':'en-US', 
             'authorization': token, 
             'content-length':'0', 
             'Cookie':f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US", 
             'origin':'https://canary.discord.com', 
             'sec-fetch-dest':'empty', 
             'sec-fetch-mode':'cors', 
             'sec-fetch-site':'same-origin', 
             'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36          ', 
             'x-context-properties':'eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==      ', 
             'x-debug-options':'bugReporterEnabled', 
             'x-super-properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}
        a = requests.post(('https://discordapp.com/api/v9/invites/' + invite), headers=headers)
        if a.status_code == 200:
            print('[+] Зашёл на сервер ' + invite + '! [' + token + ']')
        else:
            print(f"[-] Дискорд забанил твой айпи. Юзай ВПН. Ошибка: {a.text}" + ' [' + token + ']')
    except Exception as e:
        try:
            print("[-] Cloudfare забанил твой айпи. Юзай ВПН. Ошибка: " + {str(e)} + ' [' + token + ']')
        finally:
            e = None
            del e


join(inviter, tokens)