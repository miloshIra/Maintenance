import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import Spinbox





window = tk.Tk()
window.title('Vitek Maintenance')
window.geometry("500x400+50+50")


tabControl = ttk.Notebook(window)

Odrzuvanje = ttk.Frame(tabControl)
tabControl.add(Odrzuvanje, text='Odrzuvanje')
tabControl.place(x=10, y=50)

Magacin = ttk.Frame(tabControl)
tabControl.add(Magacin, text='Magacin')


window.mainloop()
