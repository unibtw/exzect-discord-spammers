from rich.console import Console
from rich.markdown import Markdown
from rich import print
import os
import json
from threading import Thread
import shutil

console = Console()

with open(os.path.join("config.json"), "r", encoding="utf8") as r_f:
    data = json.loads(r_f.read())

def starter(data):
	os.system("python3 discord_module.py -lt " + data["token_l"] + " -t " + str(data["timeout"]) + " -s " + data["server_id"] + " -c " + data["channel_id"] + " -i " + data["invite"])
	print("Запустил!")

starter(data)

