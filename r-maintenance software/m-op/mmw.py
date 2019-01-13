import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import Spinbox
import mback



class Main():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Vitek Maintenance")
        self.win.geometry("500x400+50+50")
        self.createWidgets()

    def createWidgets(self):
        tabControl = ttk.Notebook(self.win)



        tab1 = ttk.Frame(tabControl)   # -------------------------- First TAB (Odrzuvanje)
        tabControl.add(tab1, text='Одржување')
        tabControl.place(x=10, y=50)

        Label = ttk.Label(tab1, text='asdasd')
        Label.place(x=20, y=80)

        action = ttk.Button(tab1, text='Click here', command=mback.clickMe)
        action.place(x=40, y=100)

        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='Магацин')



# window = tk.Tk()
# window.title('Vitek Maintenance')
# window.geometry("500x400+50+50")
#
#
# tabControl = ttk.Notebook(window)
#
# Odrzuvanje = ttk.Frame(tabControl)
# tabControl.add(Odrzuvanje, text='Odrzuvanje')
# tabControl.place(x=10, y=50)
#
# Magacin = ttk.Frame(tabControl)
# tabControl.add(Magacin, text='Magacin')

main = Main()
main.win.mainloop()
