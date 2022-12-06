from rich.console import Console
from rich.markdown import Markdown
from rich import print
import os
import json
from threading import Thread
import shutil

console = Console()

def starter(data,path):
	os.chdir(path)
	os.system("python discord_module.py -lt " + data["token_l"] + " -st " + data["token_s"] + " -t " + str(data["timeout"]) + " -s " + data["server_id"] + " -c " + data["channel_id"])
	print("Запустил!")

def start_all():
	console.clear()
	for one in os.listdir("accounts"):
		with open(os.path.join("accounts", one, "config.json"), "r", encoding="utf8") as r_f:
			data = json.loads(r_f.read())
		agregator = Thread(target=starter, args=(data, os.path.join("accounts", one)))
		agregator.start()

def main_menu():
	console.print(Markdown("# Main menu"))
	print("[bold green] 1 [/bold green] - [bold] просмотр комбинаций [/bold]")
	print("[bold green] 2 [/bold green] - [bold] добавить комбинации [/bold]")
	print("[bold green] 3 [/bold green] - [bold] запуск выборочно [/bold]")
	print("[bold green] 4 [/bold green] - [bold] запустить все комбинации [/bold]")
	print("[bold green] 5 [/bold green] - [bold] выйти [/bold]")
	return int(input("> "))

def edit_accounts():
	console.clear()
	console.print(Markdown("# Accounts menu"))
	print("[bold green] Комбинации: [/bold green]")
	for one in os.listdir("accounts"):
		print(one)

def choise_to_start():
	console.clear()
	console.print(Markdown("# Start menu"))
	for one in os.listdir("accounts"):
		print(one)
	account = input("Введите название комбинации > ")
	if os.path.exists(os.path.join("accounts", account, "config.json")):
		with open(os.path.join("accounts", account, "config.json"), "r", encoding="utf8") as r_f:
			data = json.loads(r_f.read())
		agregator = Thread(target=starter, args=(data, os.path.join("accounts", account)))
		agregator.start()
	else:
		print("[bold red] Ошибка либо в названии комбинации, либо в комбинации не хватает элементов [/bold red]")

def add_account():
	console.clear()
	console.print(Markdown("# Add"))
	name_of_dir = input("Введите название комбинации аккаунтов > ")
	new_dir = os.path.join("accounts", name_of_dir)
	os.mkdir(new_dir)
	token_l = input("Введите токен слушателя > ")
	token_s = input("Введите токен отправителя сообщений > ")
	server_id = input("Введите id сервера > ")
	channel_id = input("Введите id канала на сервере, в котором есть все участники (необязательно онлайн, можно текстовый канал) > ")
	text_to_send = input("Введите текст для отправки в лс > ")
	timeout = int(input("Введите задержку перед обновлениями списка участников (в секундах) > "))
	with open(os.path.join(new_dir, "config.json"), "w", encoding="utf8") as w_f:
		json.dump({"token_l": token_l, "token_s": token_s, "server_id": server_id, "channel_id": channel_id, "timeout": timeout}, w_f)
	with open(os.path.join(new_dir, "text.txt"), "w", encoding="utf8") as t_f:
		t_f.write(text_to_send)
	shutil.copyfile("discord_module.py", os.path.join(new_dir, "discord_module.py"))
	shutil.copyfile("Users.txt", os.path.join(new_dir, "Users.txt"))
	shutil.copyfile("send_msg.py", os.path.join(new_dir, "send_msg.py"))
	print("[bold green] Готово! [/bold green]")

while True:
	chooise = main_menu()
	if chooise == 1:
		edit_accounts()
	elif chooise == 2:
		add_account()
	elif chooise == 3:
		choise_to_start()
	elif chooise == 4:
		start_all()
	elif chooise == 5:
		break
	else:
		print("[bold red] Я вас не понял [/bold red]")