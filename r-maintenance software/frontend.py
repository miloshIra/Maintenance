from tkinter import *
import backend
import datetime


window=Tk()
window.title('Одржување')
window.geometry("500x400+50+50")


def reporting():
    top=Toplevel()
    top.title('Пријави дефект')
    top.geometry("500x400+90+90")

    Ovar1 = StringVar(top)
    Ovar1.set("Избери")

    Ovar2 = StringVar(top)
    Ovar2.set("Избери")

    Ovar3 = StringVar(top)
    Ovar3.set("Избери")

    d1=OptionMenu(top, Ovar1, "Pletilici","Ekstruder","Bobinatura","Ekstrakcija", "Benda","Matasa","Drugo")
    d1.place(x=30, y=50, width=100, height=25)
    l1=Label(top, text="Оддел:").place(x=30, y=25, width=80, height=30)

    d2=OptionMenu(top, Ovar2, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
    d2.place(x=160, y=50, width=100, height=25)
    l2=Label(top, text="Машина:").place(x=160, y=25, width=80, height=30)

    # d3=OptionMenu(top, Ovar1, "Dragi B.","Nikola N.","Goce C.","Dalibor T.", "Igor G.","Marijan H.")
    # d3.place(x=650, y=350, width=120, height=25)
    # l3=Label(top, text="Оператор:").place(x=555, y=350, width=80, height=30)
    e1 = IntVar()
    e1 = Entry(top)
    e1.place(x=300, y=50, width=40, height=20)
    l2=Label(top, text="Оператор").place(x=286, y=25, width=80, height=30)

    e2 = StringVar()
    e2 = Entry(top)
    e2.place(x=30, y=80, width=310, height=280)

    b1=Button(top, text = 'Пријави', command = backend.save_temp_log(Ovar1, Ovar2, e2, e1 )) # Gi pokazuva predhodnite zavrsheni aktivnosti
    b1.place(x=360, y=330, width=120, height=30)

b0=Button(window,text="Пријава", command = reporting)
b0.place(x=190, y=80, width=120, height=50)



def accepting():
    top1=Toplevel()
    top1.title('Одржување')
    top1.geometry("900x440+90+90")

    l1=Listbox(top1)
    l1.place(x=20, y=20, width=650, height=380)


b11=Button(window,text="Одржување", command = accepting)
b11.place(x=190, y=150, width=120, height=50)

def engineering():
    top2=Toplevel()
    top2.title('Инженерство')
    top2.geometry("900x600+90+90")

    l2=Listbox(top2)
    l2.place(x=20, y=20, width=650, height=250)

    l3=Listbox(top2)
    l3.place(x=20, y=290, width=650, height=250)

b12=Button(window, text="Инженерство", command = engineering)
b12.place(x=190, y=220, width=120, height=50)



window.mainloop()
