import tkinter as tk
from tkinter import ttk


class Main():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Exmaple")
        self.win.geometry("500x500+50+50")
        self.createWidgets()

    def createWidgets(self):

        Labal=ttk.Label(self.win, text="Entry Box")
        Labal.place(x=30, y=50)

        name = tk.StringVar()

        nameEntered = ttk.Entry(self.win, width=17, textvariable=name)
        nameEntered.place(x=30, y=80)
        nameEntered.focus()

        button = ttk.Button(self.win, text="Done!")
        button.place(x=30, y=130)

main = Main()
main.win.mainloop()
