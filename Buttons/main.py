from tkinter import *
from tkinter import ttk

root  = Tk()

def callback(number):
    print(number)

ttk.Button(root, text="Click me 1", command = lambda: callback(1)).pack()
ttk.Button(root, text="Click me 2", command = lambda: callback(2)).pack()
ttk.Button(root, text="Click me 3", command = lambda: callback(3)).pack()

root.mainloop()
