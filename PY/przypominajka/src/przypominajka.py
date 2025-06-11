from Mylib import load_config, write_config
from przypominajka_lib import objects_to_dict
import Notatka


config = load_config()  

notes = []
for note_name, element in config.items():
    if isinstance(element, list):
        notes.append(Notatka.Notatka(note_name, element[0], element[1], element[2]))

for note in notes:
    note.alert()

# Konwertujemy z powrotem do dict
new_config = objects_to_dict(notes)
write_config(new_config) # Zapis