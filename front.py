from tkinter import *


window=Tk()
window.title('Maintenance')
window.geometry("800x900+50+50")

var1 = StringVar(window)
var1.set("")

var2 = StringVar(window)
var2.set("")

var3 = StringVar(window)
var3.set("")

var4 = StringVar(window)
var4.set("")


d1=OptionMenu(window, var1, "Dragi","Nikola","Goce","Dalibor", "Igor","Marijan").grid(row=0, column=0)
l1=Label(window, text="Оператори").grid(row=0, column=1)

d2=OptionMenu(window, var2, "Dragi","Nikola","Goce","Dalibor", "Igor","Marijan").grid(row=1, column=0)
l2=Label(window, text="Оператори").grid(row=1, column=1)

d3=OptionMenu(window, var3, "Dragi","Nikola","Goce","Dalibor", "Igor","Marijan").grid(row=0, column=3)
l3=Label(window, text="Оператори").grid(row=0, column=1)

d4=OptionMenu(window, var4, "Dragi","Nikola","Goce","Dalibor", "Igor","Marijan").grid(row=1, column=3)
l4=Label(window, text="Оператори").grid(row=1, column=1)

#t1=Text(window)
#t1.grid(row=0, column=1)

#b1=Button(window, text="Zavrshi")
#b1.grid(row=1, column=1)

#b2=Button(window, text="Zavrshi")
#b2.grid(row=2, column=2)

#b3=Button(window, text="Zavrshi")
#b3.grid(row=3, column=2)

#b4=Button(window, text="Zavrshi")
#b4.grid(row=4, column=2)

window.mainloop()
