from tkinter import *
from tkinter import ttk

root = Tk()

def mouse_press(event):
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('num: {}'.format(event.num))
    print('x: {}'.format(event.x))
    print('y: {}'.format(event.y))
    print('x_root: {}'.format(event.x_root))
    print('y_root: {}'.format(event.y_root))

canvas = Canvas(root, height = 480, width = 640).pack()
canvas.bind('<ButtonPress>', mouse_press)

root.mainloop()
