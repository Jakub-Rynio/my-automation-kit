import os 
import Edit_config
from Mylib import write_config, load_config, main_menu, file_ext, get_file_list, print_list

config = load_config("C:\\Program Files\\Czysty_Pulpit\\czysty_pulpit_config.yaml")

USERNAME = os.getlogin()
APP_PATH = config["paths"]["app_path_template"].format(username=USERNAME)
DESKTOP_PATH = config["paths"]["desktop_path_template"].format(username=USERNAME)
EXCLUDED_EXT = config["excluded_extensions"]
EXCLUDED_FILES = config["excluded_files"]
DESKTOP_FOLDER = config["desktop_folder"]
DESKTOP_FOLDER_PATH = os.path.join(DESKTOP_PATH, DESKTOP_FOLDER)

desktop_file_list = get_file_list(DESKTOP_PATH)

manager = Edit_config.Edit_config(desktop_file_list,EXCLUDED_EXT, EXCLUDED_FILES, APP_PATH, DESKTOP_FOLDER)

def new_config(new_config):
    #return  self.excluded_ext, self.excluded_files, self.app_path, self.desktop_folder
    config["excluded_extensions"] = new_config[0]
    config["excluded_files"]= new_config[1]
    config["desktop_folder"] = new_config[2]

options = ["Zamroz pulpit", "Wyswietl konfiguracje", "Edytuj", "Powrot do Domyslnej konfiguracji"]
while True:
    answer = main_menu(options)
    if answer == "exit": break
    elif answer == "1":
        manager.freeze()
        input()
    elif answer == "2":
        manager.show_config()
        
        input()
    elif answer == "3":
        manager.edit()
        input()
    elif answer == "4":
        manager.default()
        input()


new_config(manager.return_config()) 
write_config("C:\\Program Files\\Czysty_Pulpit\\czysty_pulpit_config.yaml", config)