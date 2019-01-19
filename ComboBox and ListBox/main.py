from tkinter import *
from tkinter import ttk

root = Tk()

month = StringVar()
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()
combobox.config(values = ("Jan", "Feb", "Mar", "April"))

year = StringVar()
Spinbox(root, from_ = 1990, to = 2018, textvariable = year).pack()

root.mainloop()
