#przed zastosowaniem zmienic path pliku config
import os
from datetime import datetime
import getpass
import yaml

CONFIG_FILE = "C:\\Program Files\\Przypominajka\\przypominajka_config.yaml"

def log(log, APP_FILE):
    username = getpass.getuser()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(fr"{APP_FILE}\log.txt", 'a') as f:
        f.write(f"[{now}]" + " " + f"{log} \n")

def load_config():
    with open(CONFIG_FILE, "r") as file:
        return yaml.safe_load(file)

def write_config(new_config):
    with open(CONFIG_FILE, "w") as f:
        yaml.dump(new_config, f, sort_keys=False)

def main_menu(menu_items=[]):
    os.system("cls")
    i=1
    answers = ["exit"]

    for item in menu_items:
        print(f"{i}.{item}")
        answers.append(str(i))
        i += 1
    select = ""
    while True:
        try:
            select = input(f"\nWybierz opcje\[exit] aby wyjsc: ")
            if select in answers:
                return select
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")
        except ValueError:
            print("To nie jest liczba. Spróbuj ponownie.")