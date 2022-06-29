# tk_test.py

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
from tkinter import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #configuring root window
        self.title("tk testing app")
        self.geometry('300x500')
        #label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack
        #button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command']=self.button_clicked
        self.button.pack()
        self.label1 = tk.Label(self, text="Bet")
        self.label1.pack( side = LEFT)
        self.bet_entry = tk.Entry(self, width = 8)
        self.bet_entry.insert(0,0.25)
        self.bet_entry.pack(padx = 15, pady = 15, side = RIGHT)
    def button_clicked(self):
        messagebox.showinfo(title='Information', message="Hello, Tkinter!")

if __name__ == "__main__":
    app = App()
    app.mainloop()