from tkinter import *
from tkinter import ttk
import random

root = Tk()

def __init__(self, master):
    self.master = master
    self.color = StringVar()
    self.widgets()

def change(self):
    col = '#%02x%02x%02x' %(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    self.color.set(col)
    self.preview.configure(bg = col)

def widgets(self):
    button = ttk.Button(self.master, bd = 10, text="Get Hex code", fonr=('algerian', 20), command = self.change).pack()
    ttk.Entry(self.master, textvariable = self.color, font = ('freesansbold', 20)).pack(pady = 10)
    self.preview = Frame(self.master, bd = 10, relief = 'ridge', height = 300, width = 300, bg = 'white').pack(pady = 10)

root.mainloop()