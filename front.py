from tkinter import *



window=Tk()
window.title('Maintenance')
window.geometry("800x900+50+50")

# button_names=['Осевежи','Провери','Заврши','Предходно','Помош'] promenlivi b1,b2... etc.
# buttons = range(5)
# for i in range(5):
#     b = Button(window, text=button_names[i])
#     b.place(x=650,  y=100 + i*30, width=120, height=25)

b1=Button(window, text = 'Oсвежи')
b1.place(x=650, y=20, width=120, height=30)

b2=Button(window, text = 'Провери')
b2.place(x=650, y=70, width=120, height=30)

b3=Button(window, text = 'Предходно')
b3.place(x=650, y=120, width=120, height=30)

b4=Button(window, text = 'Помош')
b4.place(x=650, y=170, width=120, height=30)

b5=Button(window, text = 'Заврши')
b5.place(x=528, y=425, width=240, height=50)

Ovar1 = StringVar(window)
Ovar1.set("Избери")

Ovar2 = StringVar(window)
Ovar2.set("Избери")


d1=OptionMenu(window, Ovar1, "Dragi B.","Nikola N.","Goce C.","Dalibor T.", "Igor G.","Marijan H.").place(x=650, y=350, width=120, height=25)
l1=Label(window, text="Оператор:").place(x=555, y=350, width=80, height=30)

d2=OptionMenu(window, Ovar2, "Dragi B.","Nikola N.","Goce C.","Dalibor T.", "Igor G.","Marijan H.").place(x=650, y=390, width=120, height=25)
l2=Label(window, text="Оператор:").place(x=555, y=390, width=80, height=30)
#
# d3=OptionMenu(window, Ovar3, "Dragi","Nikola","Goce","Dalibor", "Igor","Marijan").grid(row=0, column=2)
# l3=Label(window, text="Оператор").grid(row=0, column=1)
#
# d4=OptionMenu(window, Ovar4, "Dragi","Nikola","Goce","Dalibor", "Igor","Marijan").grid(row=1, column=2)
# l4=Label(window, text="Оператор").grid(row=1, column=1)
#
t1=Text(window)
t1.place(x=20, y=20, width=500, height=455)
#
# b1=Button(window, text="Провери")
# b1.grid(row=3, column=3)
#
# b2=Button(window, text="Заврши")
# b2.grid(row=4, column=3)


#b2=Button(window, text="Zavrshi")
#b2.grid(row=2, column=2)

#b3=Button(window, text="Zavrshi")
#b3.grid(row=3, column=2)

#b4=Button(window, text="Zavrshi")
#b4.grid(row=4, column=2)

window.mainloop()
