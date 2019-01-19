from tkinter import *
from tkinter import ttk

root = Tk()
canvas = Canvas(root)
canvas.pack()
canvas.config(height = 480, width = 640)
line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5)
canvas.itemconfig(line, fill = 'green')
canvas.coords(line)
canvas.coords(line, 0, 0, 320, 240, 640, 0)
canvas.itemconfig(line, smooth = 'True')
canvas.itemconfig(line, splinesteps = 5)


root.mainloop()
