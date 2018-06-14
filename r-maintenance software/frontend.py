from tkinter import *
import backend
import datetime


window=Tk()
window.title('Пријави дефект')
window.geometry("500x400+50+50")

b1=Button(window, text = 'Пријави') # Gi pokazuva predhodnite zavrsheni aktivnosti
b1.place(x=360, y=330, width=120, height=30)

Ovar1 = StringVar(window)
Ovar1.set("Избери")

Ovar2 = StringVar(window)
Ovar2.set("Избери")

Ovar3 = StringVar(window)
Ovar3.set("Избери")

d1=OptionMenu(window, Ovar1, "Pletilici","Ekstruder","Bobinatura","Ekstrakcija", "Benda","Matasa","Drugo")
d1.place(x=30, y=50, width=100, height=25)
l1=Label(window, text="Оддел:").place(x=30, y=25, width=80, height=30)

d2=OptionMenu(window, Ovar2, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
d2.place(x=160, y=50, width=100, height=25)
l2=Label(window, text="Машина:").place(x=160, y=25, width=80, height=30)

# d3=OptionMenu(window, Ovar1, "Dragi B.","Nikola N.","Goce C.","Dalibor T.", "Igor G.","Marijan H.")
# d3.place(x=650, y=350, width=120, height=25)
# l3=Label(window, text="Оператор:").place(x=555, y=350, width=80, height=30)
e1 = IntVar()
e1 = Entry(window)
e1.place(x=300, y=50, width=40, height=20)
l2=Label(window, text="Оператор").place(x=286, y=25, width=80, height=30)

e2 = StringVar()
e2 = Entry(window)
e2.place(x=30, y=80, width=310, height=280)













window.mainloop()
