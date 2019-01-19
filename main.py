from tkinter import *
from tkinter import ttk

class Feedback:

    def __init__(self, master):

        master.title('Explore Claifornia Feedback')
        master.resizable(False, False)
        master.configure(background='#e1d8b9')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TLabel', background='#e1d8b9', font = ('Arial', 11))
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('Header.TLabel', background='#e1d8b9', font = ('Arial', 18, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        self.logo = PhotoImage(file = "download.gif")
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = "Thanks for Exploring!", style = "Header.TLabel").grid(row=0, column=1)
        ttk.Label(self.frame_header, wraplength = 300, text = ("We're glad you chose Explore California sor your recent adventure. "
                                                               "Please tell us about what you thought about the Dsesrt to sea tour")).grid(row=1, column=1)
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = "Name").grid(row=0, column=0, padx=5, sticky = 'sw' )
        ttk.Label(self.frame_content, text="Email: ").grid(row=0, column=1, padx=5, sticky = 'sw')
        ttk.Label(self.frame_content, text="Comments: ").grid(row=2, column=0, padx=5, sticky = 'sw')

        self.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content, width=24, font = ('Arial', 10))
        self.text_comments = Text(self.frame_content, width = 50, height = 10, font = ('Arial', 10))

        self.entry_name.grid(row=1, column=0)
        self.entry_email.grid(row=1, column=1)
        self.text_comments.grid(row=3, column=0, columnspan=2)

        ttk.Button(self.frame_content, text="Submit").grid(row=4, column=0, sticky = 'e')
        ttk.Button(self.frame_content, text="Clear").grid(row=4, column=1, sticky = 'w')


def main():

    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__": main()