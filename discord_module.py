import time
import json
import discum
import argparse 
import os
import requests

ap = argparse.ArgumentParser()
ap.add_argument("-lt", "--listener-token", required=True, help="The token of listener")
ap.add_argument("-st", "--sender-token", required=True, help="The sender token")
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
def give_token():
	for i in range(0,count):
		with open('tokens.txt') as fp:
			lines = fp.readlines()
			newtoken = lines[i].split(":")[2]
			print('Взял токен ' + newtoken)
	return newtoken


take = give_token()
print('Захожу на сервер!')
os.system("python joiner.py -i " + inviter + " -t " + take)
print('Сплю ' +args["timeout"]+' секунд')
time.sleep(int(args["timeout"]))

take = give_token()
bot = discum.Client(token=take)

def close_after_fetching(resp, guild_id):
	if bot.gateway.finishedMemberFetching(guild_id):
		bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
		bot.gateway.close()

def get_members(guild_id, channel_id):
	bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1) 
	bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
	bot.gateway.run()
	bot.gateway.resetSession() 
	return bot.gateway.session.guild(guild_id).members

# guild parser 
while count == oldcount:
	with open("Users.txt", "r") as r_f:
		users_c = json.load(r_f)
	if not users_c:
		users_x = [member for member in get_members(args["server_id"], args["channel_id"])]
		print(users_x)
		with open("Users.txt", "w") as w_f:
			json.dump(users_x, w_f)
			w_f.close()
	else:
		z = ["0"]
		n_sps=""
		for i in range(powerrange1, powerrange2):
			z.append(users_c[i])
			for lst in z[1:]:
				n_sps=n_sps+lst[0]+lst[1]+lst[2]+lst[3]+lst[4]+lst[5]+lst[6]+lst[7]+lst[8]+lst[9]+lst[10]+lst[11]+lst[12]+lst[13]+lst[14]+lst[15]+lst[16]+lst[17]
				print(n_sps)
				os.system(f"python send_msg.py -id {n_sps} -t {take}")
				n_sps = ""
				z = ["0"]
				print('Сплю ' +args["timeout"]+' секунд')
				time.sleep(int(args["timeout"]))
		print('Закончил отправлять сообщения пользователям!')
		count+=1
		old = powerrange2 - powerrange1
		powerrange1 += old
		powerrange2 += old
		if oldcount != count:
			oldcount +=1
		take = give_token()
		print('Захожу на сервер!')
		os.system("python joiner.py -i " + inviter + " -t " + take)
		print('Сплю ' +args["timeout"]+' секунд')
		time.sleep(int(args["timeout"]))
