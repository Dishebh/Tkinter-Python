from tkinter import *
from tkinter import ttk

class main:
    def __init__(self, master):
        self.master = master
        self.n = StringVar()
        self.widgets()

    def get(self):
        m = self.n.get()
        self.ara.delete("1.0",END)
        for i in range(20):
            self.ara.insert(END,(m + ' X ' + i + ' = ' + str(int(m) * i)))
            self.ara.insert(END,'\n')

    def widgets(self):
        Entry(self.master, bd=10, bg = 'aqua', font = ('width', 20, 'bold'), width = 10, textvariable = self.n).pack()
        Button(self.master, bd=10, text = 'Get Table', font = ('arial', 25, 'bold'), bg = 'red', command = self.get).pack()
        self.ara = Text(self.master, bd=10, height = 10, width = 25, bg = 'green', font = ('arial', 20, 'bold'), state=NORMAL).pack()






root = Tk()
root.config(background = 'black')
root.title('Multiplication Table')
main(root)
root.mainloop()