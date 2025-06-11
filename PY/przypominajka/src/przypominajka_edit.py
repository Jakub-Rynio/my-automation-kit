from Mylib import load_config, main_menu
from przypominajka_lib import show_note, write, add_note, refresh_note_names
import Notatka_Edit
import os

config = load_config()  
menu_items = ["Edytuj Notatke", "Wyswietl Notatke", "Dodaj notatke", "Usun Notatke"]

notes = [] # List of note obj
for note_name, element in config.items():
    if isinstance(element, list):
        notes.append(Notatka_Edit.Notatka_Edit(note_name, element[0], element[1], element[2]))

note_names = []
for note in notes:
    note_names.append(note.get_note_name())

def main_loop():
    while True:
        option = main_menu(menu_items)
        if option == "exit": break
        elif option == "1":
            note_names = refresh_note_names(notes)
            item = main_menu(note_names)
            if item == "exit":
                continue
            else: 
                item = int(item)
                note_obj = notes[item - 1]
            show_note(note_obj)
            note_obj.edit()
            write(notes)
            input()

        if option == "2": 
            os.system("cls")
            for note in notes:
                show_note(note)
            input()

        if option == "3": 
            os.system("cls")
            note_names = refresh_note_names(notes)
            notes.append(Notatka_Edit.Notatka_Edit(*add_note(note_names)))
            write(notes)
            input()

        if option == "4": 
            note_names = refresh_note_names(notes)
            item = main_menu(note_names)
            if item == "exit":
                continue
            else: 
                item = int(item)
                del notes[item -1]
                write(notes)
            input()
main_loop()
