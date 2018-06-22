from tkinter import *
import backend
import datetime
import uuid

window=Tk()
window.title('Одржување')
window.geometry("500x400+50+50")


def add_reporting():
    top=Toplevel()
    top.title('Пријави дефект')
    top.geometry("500x400+90+90")

    def add_reporting_command():
        backend.save_temp_log(oddel.get(), broj_na_mashina.get(), opis.get(), broj_na_operator.get())
        top.destroy()

    b1=Button(top, text ='Пријави', command=add_reporting_command) # Gi pokazuva predhodnite zavrsheni aktivnosti
    b1.place(x=360, y=330, width=120, height=30)

    oddel = StringVar(top)
    oddel.set("Избери")

    broj_na_mashina = IntVar(top)
    broj_na_mashina.set("Избери")

    # Ovar3 = StringVar(top)
    # Ovar3.set("Избери")

    d1=OptionMenu(top, oddel, "Pletilici","Ekstruder","Bobinatura","Ekstrakcija", "Benda","Matasa","Drugo")
    d1.place(x=30, y=50, width=100, height=25)
    l1=Label(top, text="Оддел:").place(x=30, y=25, width=80, height=30)

    d2=OptionMenu(top, broj_na_mashina, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
    d2.place(x=160, y=50, width=100, height=25)
    l2=Label(top, text="Машина:").place(x=160, y=25, width=80, height=30)

    # d3=OptionMenu(top, Ovar1, "Dragi B.","Nikola N.","Goce C.","Dalibor T.", "Igor G.","Marijan H.")
    # d3.place(x=650, y=350, width=120, height=25)
    # l3=Label(top, text="Оператор:").place(x=555, y=350, width=80, height=30)
    broj_na_operator = StringVar()
    e1 = Entry(top, textvariable=broj_na_operator)
    e1.place(x=300, y=50, width=40, height=20)
    l2=Label(top, text="Оператор").place(x=286, y=25, width=80, height=30)

    opis = StringVar()
    e2 = Entry(top, textvariable=opis)
    e2.place(x=30, y=80, width=310, height=280)


b0=Button(window, text="Налог", command = add_reporting)
b0.place(x=190, y=80, width=120, height=50)



def maintaining():
    top1=Toplevel()
    top1.title('Одржување')
    top1.geometry("900x440+90+90")

    def proveri_nalozi():
        l1.delete(0,END)
        for row in backend.view_temp_logs():
            # current_row = row['Oddel'] + " - " + row['broj'] + " - " +  row['opis']  + " - " +  row['data']  + " - " +  row['operator']# + ", " + row['Mashina']
            l1.insert(END, row)

    def prevzemi_nalog():
        x=l1.get(l1.curselection())
        print(x[0])
        z=uuid.uuid4().hex
        print(z)
        backend.started_working()

    bm1=Button(top1, text="Превземи", command=prevzemi_nalog)
    bm1.place(x=715, y=20, width=140, height=50)

    bm2=Button(top1, text="Заврши")
    bm2.place(x=715, y=350, width=140, height=50)

    bm3=Button(top1, text="Види", command = proveri_nalozi)
    bm3.place(x=715, y=100, width=140, height=50)

    bm4=Button(top1, text="Затвори")
    bm4.place(x=715, y=200, width=140, height=50)

    l1=Listbox(top1, selectmode=EXTENDED)
    l1.place(x=20, y=20, width=650, height=380)



b11=Button(window,text="Одржување", command = maintaining)
b11.place(x=190, y=150, width=120, height=50)

def engineering():
    top2=Toplevel()
    top2.title('Инженерство')
    top2.geometry("900x600+90+90")

    def proveri_nalozi():
        l2.delete(0,END)
        print(l2.curselection())
        for row in backend.view_temp_logs():
            # current_row = row['Oddel'] + " - " + row['broj'] + " - " +  row['opis']  + " - " +  row['data']  + " - " +  row['operator']# + ", " + row['Mashina']
            l2.insert(END, row)

    # def prevzemi_nalog():
    #     backend.started_working()



    l2=Listbox(top2)
    l2.place(x=20, y=20, width=650, height=250)


    l3=Listbox(top2)
    l3.place(x=20, y=290, width=650, height=250)

    b31=Button(top2, text="Види", command = proveri_nalozi )
    b31.place(x=730, y=50, width=120, height=50)


b12=Button(window, text="Инженерство", command = engineering)
b12.place(x=190, y=220, width=120, height=50)



window.mainloop()
