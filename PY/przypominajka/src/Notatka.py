from datetime import date
import tkinter as tk
from tkinter import messagebox

class Notatka:
    def __init__(self,note_name ,date, message, repeat_days):
        self.note_name = note_name
        self.date = date
        self.message = message
        self.repeat_days = repeat_days
        self.TODAY = date.today()
        self.DELTA_TIME = self.date - self.TODAY
        self.root = tk.Tk()
        self.window = tk.Toplevel()

    def __one_month_from_now(self):
        if 7 <= self.DELTA_TIME.days <= 30:
            return True
        
    def __one_wick_from_now(self):
        if self.DELTA_TIME.days <= 7:
            return True

    def __show_message(self, message):
        try:
            self.root.withdraw()
            self.window
            messagebox.showinfo("🔔 Przypomnienie", message)
            self.root.destroy()
        except:
            return None

    def alert(self):
        message = f"Do zadania:\n\t{self.message}\nZaplanownaego na:\n\t{self.date}\nZostalo:\n\t {self.DELTA_TIME.days} dni"

        if self.__one_month_from_now() and self.repeat_days > 0:
            self.__show_message(message)
            self.repeat_days -= 1
        elif self.__one_wick_from_now():
            self.__show_message(message)