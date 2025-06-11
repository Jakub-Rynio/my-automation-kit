#przed zastosowaniem zmienic path pliku config
import os
from datetime import datetime
import time
import shutil
import getpass
import yaml

def log(log, APP_FILE):
    username = getpass.getuser()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(fr"{APP_FILE}\log.txt", 'a') as f:
        f.write(f"[{now}]" + " " + f"{log} \n")

# skladnia wersji teta jest taka: TETA Aplikacja klienta - 32.41
# ta funkcja pobiera najwieksza wersje jaka jest w folderze 
def latest_version(path):
    numbers = []
    
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            czesc = name.rsplit(" ", 1)[-1]  # Wyciągamy część po ostatniej spacji
            try:
                numbers.append(float(czesc))  # Próba konwersji na float
            except ValueError:
                pass  # Jeśli nie uda się, pomijamy ten folder

    latest_version =  max(numbers) if numbers else None  # Zwracamy największą liczbę, jeśli są jakiekolwiek liczby
    return str(latest_version)


def get_folder_timestamp(path):
    return os.path.getmtime(path)

def save_timestamp(timestamp, file_path):
    with open(file_path, 'w') as f:
        f.write(str(timestamp))


def read_saved_timestamp(file_path):
    try:
        with open(file_path, 'r') as f:
            saved_timestamp = f.read().strip()
            return float(saved_timestamp)
    except FileNotFoundError:
        return None

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        log(f"Plik zostal skopiowany do {destination}")
    except Exception as e:
        log(f"Blad podczas kopiowania pliku: {e}")

def print_list(list):
    for item in list: print(item)
    input()

def get_file_list(folder_path):
    file_list = []
    dir_list = os.listdir(folder_path)
    for item in dir_list:
        item_copy = item
        if os.path.isfile(os.path.join(folder_path, item_copy)):
            file_list.append(item)
    return file_list

def file_ext(filename):
    _, ext = os.path.splitext(filename)
    ext = ext.lstrip('.')  
    return ext

def load_config(config_file):
    with open(config_file, "r") as file:
        return yaml.safe_load(file)

def write_config(config_file, config):
    with open(config_file, "w") as f:
        yaml.dump(config, f, sort_keys=False)

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
            select = input(f"\nWybierz opcje [exit] aby wyjsc: ")
            if select in answers:
                return select
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")
        except ValueError:
            print("To nie jest liczba. Spróbuj ponownie.")