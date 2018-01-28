import datetime
import sqlite3
import pandas as p

#IS PANDAS DATAFRAME MUTABLE OR IS IT A TUPPLE !!!!!??!!?!?!?

link=sqlite3.connect("Records.db")
cur=link.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Stored (id INTEGER PRIMARY KEY, Oddel text, Mashina text, Aktivnost text, Data text, Operatori text  )")
link.commit()
link.close()       # Creates a table ako ne postoi ako postoi nisto ... ova ke se brishe izgleda ke ostane samo konekcijata ??



def update(Oddel, Mashina, Aktivnost, Data, Operatori):
    link=sqlite3.connect("Records.db")
    cur=link.cursor()
    cur.execute("INSERT INTO Stored VALUES(NULL,?,?,?,?,?)",(Oddel,Mashina,Aktivnost,Data,Operatori))
    link.commit()
    link.close()

update('Pletilici','1','1','21.2.2018','Nikola')

asd=sqlite3.connect("Records.db")
df=p.read_sql_query("SELECT * FROM Stored", asd)


def zapisi():
    # z = str(datetime.datetime.now())
    # f = open('database.csv', 'w')
    # f.write(z)
    # print(z)
    link=sqlite3.connect("Records.db")
    cur=link.cursor()
    cur.execute("SELECT * FROM Stored")
    rows=cur.fetchall()
    link.close()
    return rows
zapisi()

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


# print(check())
