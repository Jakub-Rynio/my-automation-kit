import os
from Mylib import log, file_ext, load_config
import shutil

def main():
    config = load_config()
    USERNAME = os.getlogin()
    APP_PATH = config["paths"]["app_path_template"].format(username=USERNAME)
    DESKTOP_PATH = config["paths"]["desktop_path_template"].format(username=USERNAME)
    EXCLUDED_EXT = config["excluded_extensions"]
    EXCLUDED_FILES = config["excluded_files"]
    DESKTOP_FOLDER = config["desktop_folder"]
    DESKTOP_FOLDER_PATH = os.path.join(DESKTOP_PATH, DESKTOP_FOLDER)

    items_list = os.listdir(DESKTOP_PATH)
    filtred_files = []
    files_ext = []
    file_path = {}

    # Robi plik Pulpit
    if not os.path.exists(DESKTOP_FOLDER_PATH):
            os.makedirs(DESKTOP_FOLDER_PATH)
            log(f"Folder {DESKTOP_FOLDER} zostal zrobiony w lokalizacji {DESKTOP_PATH}", APP_PATH)

    #Filtruje pliki i rozszezenia 
    for item in items_list:
        if os.path.isfile(os.path.join(DESKTOP_PATH,item)) and file_ext(item) not in EXCLUDED_EXT:
            filtred_files.append(item)
            files_ext.append(file_ext(item))

    # Robi foldery w pliku pulpit na pulpicie
    for item in list(set(files_ext)):
        file_path[item] = os.path.join(DESKTOP_FOLDER_PATH,item)
        if not os.path.exists(os.path.join(DESKTOP_FOLDER_PATH,item)):
            os.makedirs(os.path.join(DESKTOP_FOLDER_PATH,item))
            log(f"Folder {item} zostal zrobiony w lokalizacji {DESKTOP_FOLDER_PATH}", APP_PATH)

    #Przenosi pliki do folderow
    for item in filtred_files:
        ext = file_ext(item)
        if ext in file_path:
            if (not os.path.exists(os.path.join(file_path[ext],item))) and item not in EXCLUDED_FILES:
                shutil.move(os.path.join(DESKTOP_PATH,item), file_path[ext])
                log(f"Plik {item} =======> {file_path[ext]}", APP_PATH)
            else: log(f"Plik {item} juz istnieje w {file_path[ext]}", APP_PATH)

if __name__ == "__main__":
    main()