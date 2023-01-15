import time
import json
import discum
import argparse 
import os

ap = argparse.ArgumentParser()
ap.add_argument("-lt", "--listener-token", required=True, help="The token of listener")
ap.add_argument("-t", "--timeout", required=True, help="The timeout in seconds")
ap.add_argument("-s", "--server-id", required=True, help="The server id")
ap.add_argument("-c", "--channel-id", required=True, help="The channel id")	
ap.add_argument("-i", "--invite", required=True, help="The channel id")	

args = vars(ap.parse_args())

inviter = args['invite']
take = args['listener_token']

print('Захожу на сервер!')
os.system("python3 joiner.py -i " + inviter + " -t " + take)


bot = discum.Client(token=args["listener_token"])


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


while True:
	with open("Users.txt", "r") as r_f:
		users_c = json.load(r_f)
	if not users_c:
		users_x = [member for member in get_members(args["server_id"], args["channel_id"])]
		print(users_x)
		with open("Users.txt", "w") as w_f:
			json.dump(users_x, w_f)
			w_f.close()
	time.sleep(int(args["timeout"]))


