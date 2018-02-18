from tkinter import *
import datetime
import back


# def check_time():   # This should read the databace date and compare it with the current date and print the outdated resutls... :(
#     for row in back.zapisi():
#

def view_stored():    # Prints the database in the Listbox
    l2.delete(0,END)
    for index, row in back.iterrows():
        print(row)
        current_row = row['Oddel'] + " - " + row['Mashina'] + " - " +  row['Aktivnost']  + " - " +  row['Data']  + " - " +  row['Operatori']# + ", " + row['Mashina']
        l2.insert(END, current_row)
    #l2.insert(END,back.df)


#
# def zapis():
#     f = open('database.csv', 'w')
#     z = str(datetime.datetime.now())
#     f.write(z)
#     print(z)
#     l1.insert(END,z)


window=Tk()
window.title('Maintenance')
window.geometry("800x900+50+50")

b1=Button(window, text = 'Предходно', command=view_stored) # Gi pokazuva predhodnite zavrsheni aktivnosti
b1.place(x=650, y=20, width=120, height=30)

b2=Button(window, text = 'Провери') # Placeholder ne znam sto ke pravi
b2.place(x=650, y=70, width=120, height=30)

b3=Button(window, text = 'Освежи') # ja proveruva celata databaza spored segashiot datum
b3.place(x=650, y=120, width=120, height=30)

def add_new():
    top = Toplevel()
    top.title("Додавање нова машина")
    top.geometry("650x200+150+150")
    bu1=Button(top, text="Додај")
    bu1.place(x=500, y=500, width=120, height=30)
    bu2=Button(top, text="Откажи")

    Ovar3 =StringVar(top)
    Ovar3.set("Оддел")

    Ovar4 = StringVar(top)
    Ovar4.set("Број")

    d3=OptionMenu(top, Ovar3, "Pletilici","Estruder","Benda/Sbenda","Bobinatura", "Matasa","Ekstrakcija").place(x=650, y=350, width=120, height=25)
    d4=OptionMenu(window, Ovar4, "1","2","3","4", "5","6","7","8","9","10", "11","12", "13","14","15","16", "17","18", "19","20","21","22","23","24","25","26", "27","28", "29","30",,"31","32", "33","34", "35","36","37","38", "39","40", "41","42","43","44", "45","46", "47","48","49","50").place(x=650, y=390, width=120, height=25)



b4=Button(window, text = 'Додај', command=add_new)
b4.place(x=650, y=170, width=120, height=30) # Ke додава нови машини во датабаза


b5=Button(window, text = 'Заврши') # Ke pravi zapis od zavrshen aktivnost so momentalniot datum i vreme
b5.place(x=528, y=425, width=240, height=50)

Ovar1 = StringVar(window)
Ovar1.set("Избери")

Ovar2 = StringVar(window)
Ovar2.set("Избери")

d1=OptionMenu(window, Ovar1, "Dragi B.","Nikola N.","Goce C.","Dalibor T.", "Igor G.","Marijan H.").place(x=650, y=350, width=120, height=25)
l1=Label(window, text="Оператор:").place(x=555, y=350, width=80, height=30)

d2=OptionMenu(window, Ovar2, "Dragi B.","Nikola N.","Goce C.","Dalibor T.", "Igor G.","Marijan H.").place(x=650, y=390, width=120, height=25)
l2=Label(window, text="Оператор:").place(x=555, y=390, width=80, height=30)

l1=Listbox(window)
l1.place(x=20, y=20, width=500, height=455)


sb1=Scrollbar(window)
sb1.place(x=500, y=20, width=20, height=455)
sb1.configure(command=l1.yview)
l1.configure(yscrollcommand=sb1.set)


l2=Listbox(window)
l2.place(x=20, y=520, width=755, height=360)


window.mainloop()
