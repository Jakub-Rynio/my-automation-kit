from datetime import date
from datetime import datetime, date
from typing import Union
from dateutil.relativedelta import relativedelta
from Mylib import main_menu
import os

class Notatka_Edit:
    def __init__(self,note_name, date, message, repeat_days):

        self.note_name = note_name
        self.date = date
        self.message = message
        self.repeat_days = repeat_days
        self.TODAY = date.today()
        self.DELTA_TIME = self.date - self.TODAY

    def get_note_name(self) -> str: return self.note_name
    def get_date(self) -> date: return self.date
    def get_message(self) -> str: return self.message
    def get_repeat_days(self) -> int: return self.repeat_days
    def get_left_days(self) -> int: return self.DELTA_TIME.days

    def __change(self, item) -> Union[int,date,str]:
            os.system("cls")
            if isinstance(item, date):
                print("Podaj date w formacie dd-mm-rrrr")
                while True:
                    try:
                        new = input(f"Stara Wartosc: {item}\nPodaj nowa nazwe[exit]aby anulowac: ")
                        if new == "exit": return item
                        new_date = datetime.strptime(new, "%d-%m-%Y").date()
                        return new_date
                    except:
                        print("Nieprawidlowy fromat")
            elif isinstance(item, int):
                while True:
                    try:
                        new = input(f"Stara Wartosc: {item}\nPodaj nowa nazwe[exit]aby anulowac: ")
                        if new == "exit": return item
                        new = int(new)
                        if new < 0 or new > 24:
                            print("Podaj liczba od 0 do 24")
                            continue
                        return new
                    except:
                        print("Nieprawidlowy fromat")

            new = input(f"Stara Wartosc: {item}\nPodaj nowa nazwe[exit]aby anulowac: ")
            if new == "exit": return item
            else: return new

    def edit(self):
        menu_items = ["Zmnien nazwe", "Zmien date", "Zmien wiadomosc", "Dni wyswietlania miesiac przed", "Przenies na przyszly miesiac", "Przenies na przyszly rok"]

        option = ""
        while option != "exit":
            option = main_menu(menu_items)

            if option == "exit": continue
            else: option = int(option)

            if option == 1: self.note_name = self.__change(self.note_name)
            elif option == 2: self.date = self.__change(self.date)
            elif option == 3: self.message = self.__change(self.message)
            elif option == 4: self.repeat_days = self.__change(self.repeat_days)
            elif option == 5: self.date = self.date + relativedelta(months=1)
            elif option == 6: self.date = self.date + relativedelta(years=1)