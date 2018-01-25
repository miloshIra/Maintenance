import datetime
import sqlite3

def link():
    link=sqlite3.connect("Records.db")
    cur=link.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Stored (id INTEGER PRIMARY KEY, Oddel text, Mashina text, Aktivnost text, Data text, Operatori text  )")
    link.commit()
    link.close()

# def zapis():
#     z = str(datetime.datetime.now())
#     f = open('database.csv', 'w')
#     f.write(z)
#     print(z)
#     l1.insert(END,z)
#
# zapis()

def update(Oddel, Mashina, Aktivnost, Data, Operatori):
    link=sqlite3.connect("Records.db")
    cur=link.cursor()
    cur.execute("INSERT INTO Stored VALUES(NULL,?,?,?,?,?)",(Oddel,Mashina,Aktivnost,Data,Operatori))
    link.commit()
    link.close()

def delete(id):
    link=sqlite3.connect("Records.db")
    cur=link.cursor()
    cur.execute("DELETE FROM Stored WHERE id=?",(id,))
    link.commit()
    link.close()

def check():
    link=sqlite3.connect("Records.db")
    cur=link.cursor()
    cur.execute("SELECT * FROM Stored")
    rows=cur.fetchall()
    link.close()
    return rows

delete(1)

link()
update('Pletilici','1','1','21.2.2018','Nikola')
print(check())
