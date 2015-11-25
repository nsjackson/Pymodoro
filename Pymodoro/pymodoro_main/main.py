#! /usr/bin/python

from tkinter import *


class PymodoroApp:

    def __init__(self, root):
        self.root = root
        root.title("Pymodoro Timer")

        self.mainframe = Frame(root)
        self.mainframe.grid(column=0, row=0)
        self.mainframe.pack()

        self.user_label = Label(self.mainframe, text="User:")
        self.user_label.grid(column=0, row=0)
        self.user_label.pack()

        self.users_listbox = Listbox(self.mainframe)
        self.users_listbox.grid(column=1, row=0)
        self.users_listbox.pack()

        self.close_button = Button(self.mainframe, text="Close", command=root.quit)
        self.close_button.pack()

if __name__ == "__main__":
    master = Tk()
    app = PymodoroApp(master)
    master.mainloop()
