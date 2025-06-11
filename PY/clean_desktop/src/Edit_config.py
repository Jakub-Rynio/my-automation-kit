from Mylib import main_menu, print_list
import os

class Edit_config:
    def __init__(self, desktop_file_list, EXCLUDED_EXT=[], EXCLUDED_FILES=[], APP_PATH="", DESKTOP_FOLDER=""):
        self.desktop_file_list = desktop_file_list
        self.excluded_ext = EXCLUDED_EXT
        self.excluded_files = EXCLUDED_FILES
        self.app_path = APP_PATH
        self.desktop_folder = DESKTOP_FOLDER

    def __add_ext(self):
        while True:
            os.system("cls")
            ext = input("Podaj nazwe rozszerzenia: ")
            if ext not in self.excluded_ext:
                self.excluded_ext.append(ext)
                break
            else: 
                print("takie rozszerzenie juz istnieje")
                continue

    def __add_file(self):
        file = input("Podaj nazwe: ")
        if file in self.desktop_file_list:
            self.excluded_files.append(file)
        elif file not in self.desktop_file_list:
            os.system("cls")
            while True:
                ans = input("takiego pliku nie ma na pulpicie, czy napewno chcesz go dodac? n/t: ")
                if ans == "t":
                    self.excluded_files.append(file)
                    break
                elif ans == "n": break
                else: continue
        else: print("Nie mozna dodac rozszerzenia")
        
    def __delete_list_item(self, list):
        index = main_menu(list)
        while True:
            if index == "exit": break
            else:
                try:
                    index = int(index)
                    del list[index - 1]
                    break
                except:
                    break

    def show_config(self):
        options = ["Wykluczone rozszerzenia", "Wykluczone Pliki", "Konfiguracja"]
        while True:
            os.system("cls")
            answer = main_menu(options)
            if answer == "exit": break
            elif answer == "1": print_list(self.excluded_ext)
            elif answer == "2": print_list(self.excluded_files)
            elif answer == "3": 
                print(f"Aplikacja znajduje sie w {self.app_path}\n Folder docelowy plikow Nazywa sie: {self.desktop_folder}")
                input()
            
    def edit(self):

        options = ["Edytuj rozszerzenia", "Edytuj wykluczone Pliki", "Edytuj Konfiguracje"]
        basic_options = ["Dodaj", "Usun"]
        while True:
            os.system("cls")
            selected_option = main_menu(options)
            if selected_option == "exit": break
            elif selected_option == "1": 
                answer = main_menu(basic_options)
                if answer == "exit": break
                elif answer == "1":
                    self.__add_ext()
                    break
                elif answer == "2":
                    self.__delete_list_item(self.excluded_ext)
                    break
            elif selected_option == "2": 
                answer = main_menu(basic_options)
                if answer == "exit": break
                elif answer == "1":
                    self.__add_file()
                    break
                elif answer == "2": 
                    self.__delete_list_item(self.excluded_files)
                    break
            elif selected_option == "3":
                new = input("Podaj nowa nazwe pliku konfiguracyjnego [exit] aby wyjsc: ")
                if new == "exit": break
                self.desktop_folder = new

    def freeze(self):
        self.excluded_files = list(set(self.desktop_file_list) | set(self.excluded_files))
    def default(self):
        self.excluded_ext = [ "lnk", '{ED7BA470-8E54-465E-825C-99712043E01C}', '{4234d49b-0245-4df3-b780-3893943456e1}', "url", "ini"]
        self.excluded_files = []
   
    def return_config(self):
        return  self.excluded_ext, self.excluded_files, self.desktop_folder