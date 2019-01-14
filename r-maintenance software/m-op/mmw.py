import tkinter as tk
from tkinter import ttk

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
        tabControl.pack(expand=1, fill="both")

        tabControl.add(tab1, text='Одржување')



        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='Магацин')

        FrameT1 = ttk.LabelFrame(tab1, text="Налози и историја") # ---------- Frame label doesnt show without Labels !!
        FrameT1.grid(column=0, row=0, padx=10, pady=10)
        ttk.Label(FrameT1, text="Enter a name:").grid(column=0, row=0)

        Label = ttk.Label(FrameT1, text='A Button!!')
        Label.grid(column=1, row=1)

        action = ttk.Button(FrameT1, text='Click here', command=mback.clickMe)
        action.grid(column=2, row=2)

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
