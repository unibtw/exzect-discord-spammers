from rich.console import Console
from rich.markdown import Markdown
from rich import print
import os
import json
from threading import Thread
import shutil

console = Console()

def starter(data):
	os.system("python3 discord_module.py" + " -t " + str(data["timeout"]) + " -s " + data["server_id"] + " -c " + data["channel_id"] + " -i " + data["invite"] + " -r1 " + str(data['range1']) + " -r2 " + str(data['range2']))

with open(os.path.join("config.json"), "r", encoding="utf8") as r_f:
    data = json.loads(r_f.read())

starter(data)