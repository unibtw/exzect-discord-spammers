import discum
import argparse 

ap = argparse.ArgumentParser()
ap.add_argument("-id", "--indeficator", required=True, help="The id of user")
ap.add_argument("-t", "--token", required=True, help="The token of sender user")

args = vars(ap.parse_args())

with open("text.txt", "r", encoding="utf8") as r_f:
	text_to_send = r_f.read()

bot = discum.Client(token=args["token"])

newDM = bot.createDM([args["indeficator"]]).json()["id"] 
bot.sendMessage(newDM, text_to_send)