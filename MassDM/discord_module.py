import time
import json
import discum
import argparse 
import os
import requests
import re
import random

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--timeout", required=True, help="The timeout in seconds")
ap.add_argument("-s", "--server-id", required=True, help="The server id")
ap.add_argument("-c", "--channel-id", required=True, help="The channel id")	
ap.add_argument("-i", "--invite", required=True, help="The invite link")
ap.add_argument("-r1", "--range1", required=True, help="The first range")	
ap.add_argument("-r2", "--range2", required=True, help="The second range")	

args = vars(ap.parse_args())

oldcount = 1
count = 1
inviter = args['invite']
timouter = args['timeout']
powerrange1 = int(args['range1'])
powerrange2 = int(args['range2'])
with open(os.path.join("config.json"), "r", encoding="utf8") as r_f:
    data = json.loads(r_f.read())

def give_token():
	for i in range(0,count):
		with open('tokens.txt') as fp:
			lines = fp.readlines()
			if data['token_type'] == '1':
				newtoken = lines[i]
			elif data['token_type'] == '2':
				newtoken = lines[i].split(":")[2]
	print(f'Взял токен {newtoken[:36]}*****')
	return newtoken


take = give_token()
print('Захожу на сервер!')
os.system("python3 joiner.py -i " + inviter + " -t " + take)

# with open ('proxy.txt', 'r') as file:
#     lines = file.readlines()
#     proxer = random.choice(lines)

# proxyip = proxer.split(":")[0]
# proxyport = proxer.split(":")[1]

take = give_token()
# bot = discum.Client(token=take, proxy_host=proxyip, proxy_port=proxyport)

# def close_after_fetching(resp, guild_id):
# 	if bot.gateway.finishedMemberFetching(guild_id):
# 		bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
# 		bot.gateway.close()

# def get_members(guild_id, channel_id):
# 	bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1) 
# 	bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
# 	bot.gateway.run()
# 	bot.gateway.resetSession() 
# 	return bot.gateway.session.guild(guild_id).members

# guild parser 
while count == oldcount:
	if data['type'] == '2':
		with open("Users.txt", "r") as mab:
			userw = json.load(mab)
	with open("Users.txt", "r") as r_f:
		userss1 = r_f.readlines()
	if not userss1:
		print('У вас пустой файл Users.txt!')
		break
	else:
		z = ["0"]
		n_sps=""
		for g in range(powerrange1, powerrange2):
			if data['type'] == '1':
				with open('Users.txt') as fp:
					userss = fp.readlines()
					newuser2 = userss[g]
				print('Взял пользователя ' + newuser2)
				os.system(f"python3 send_msg.py -id {int(newuser2)} -t {take}")
				# print('Сплю ' +args["timeout"]+' секунд')
				# time.sleep(int(args["timeout"]))
			elif data['type'] == '2':
				z.append(userw[g])
				for lst in z[1:]:
					n_sps=n_sps+lst[0]+lst[1]+lst[2]+lst[3]+lst[4]+lst[5]+lst[6]+lst[7]+lst[8]+lst[9]+lst[10]+lst[11]+lst[12]+lst[13]+lst[14]+lst[15]+lst[16]+lst[17]
					print('Взял пользователя ' + n_sps)
					os.system(f"python3 send_msg.py -id {n_sps} -t {take}")
					n_sps = ""
					z = ["0"]
		print('Закончил отправлять сообщения пользователям!')
		count+=1
		if data['type'] == '2':
			old = powerrange2 - powerrange1
			powerrange1 += old
			powerrange2 += old
		if oldcount != count:
			oldcount +=1
		take = give_token()
		print('Захожу на сервер!')
		os.system("python3 joiner.py -i " + inviter + " -t " + take)