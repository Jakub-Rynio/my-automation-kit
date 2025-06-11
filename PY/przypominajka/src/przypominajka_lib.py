from Mylib import write_config
from datetime import datetime, date
from typing import Optional
import os

def objects_to_dict(notes_list):
    result = {}
    for i, note_obj in enumerate(notes_list):
        key = note_obj.note_name
        result[key] = [note_obj.date, note_obj.message, note_obj.repeat_days]
    return result

def show_note(note):
    print(f"{note.get_note_name()}\n\tZaplanowano na: {note.get_date()} | Zostalo: {note.get_left_days()} Dni\n\tTresc:{note.get_message()}\n\tPrzypomnienia 30 dni przed terminem: {note.get_repeat_days()}")

def write(notes):
    new_config = objects_to_dict(notes)
    write_config(new_config) # Zapis

def get_str(message):
    out = str(input(message))
    return out 

def get_repeat_days(message):
    while True:
        try:
            out = int(input(message))
            if out < 0 or out > 24:
                print("Podaj liczbe od 0 do 24")
                continue
            return out
        except:
            print("Nieprawidlowy fromat")

def get_date(message):

    while True:
        try:
            out = (input(message))
            out = datetime.strptime(out, "%d-%m-%Y").date()
            return out
        except:
            print("Nieprawidlowy fromat")

def add_note(name_list=[]):
    try:
        os.system("cls")
        print("Dodawanie Notatki: ")
        note_name = get_str("Podaj nazwe Notatki: ")
        if note_name in name_list or note_name == "":
            raise ValueError("Juz istnieje taka notatka")
        date = get_date("Podaj date w formacie dd-mm-rrrr: ")
        message = get_str("Podaj tresc notatki: ")
        repeat_days = get_repeat_days("przez ile dni miesiac przed wyswietlac komunikat: ")
        return note_name, date, message, repeat_days

    except ValueError as e:
        print(f"Wystapil blad: {e}")

def refresh_note_names(notes) -> Optional[list[str]]:
    note_names =[]
    for note in notes:
        note_names.append(note.get_note_name())
    return note_names

    