import datetime
import pandas as p
import psycopg2 as psy



link =psy.connect("dbname='forumdb' user='postgres' password='post' host='localhost' port='5432'")
cur=link.cursor()
cur.execute("DROP TABLE Machines")
cur.execute("DROP TABLE Activity")
cur.execute("DROP TABLE Machine_Activity")
cur.execute("CREATE TABLE IF NOT EXISTS Machines (Oddel TEXT, Broj INTEGER )")
cur.execute("CREATE TABLE IF NOT EXISTS Activity (Oddel TEXT, Broj INTEGER, Ime TEXT, Frekfentnost INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS Machine_Activity (Oddel TEXT, Mashina_id INTEGER, Aktivsnot_id INTEGER, Frekfentnost INTEGER, Data DATE, Operator TEXT)")
link.commit()
link.close()   # Creates a table ako ne postoi ako postoi nisto ... ova ke se brishe izgleda ke ostane samo konekcijata ??

def add_machine(Oddel, Broj):
    link =psy.connect("dbname='forumdb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("INSERT INTO Machines VALUES(%s,%s)",(Oddel, Broj))
    link.commit()
    link.close()  # This must later transform into a machine adding function


add_machine('Pletilici',1)
add_machine('Pletilici',2)
add_machine('Pletilici',3)
add_machine('Pletilici',5)
add_machine('Pletilici',6)
add_machine('Pletilici',7)
add_machine('Pletilici',8)

def add_activity(Oddel, Broj, Ime, Frekfentnost):
    link =psy.connect("dbname='forumdb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()     #Oddel TEXT, Broj INTEGER, Ime TEXT, Frekfentnost INTEGER
    cur.execute("INSERT INTO Activity VALUES (%s,%s,%s,%s)", (Oddel, Broj, Ime, Frekfentnost))
    link.commit()
    link.close()

add_activity('Pletilici', 1, 'Bela', 15)
add_activity('Pletilici', 2, 'Kafena', 30)
add_activity('pletilici', 3, 'Crna', 180)

def record_keep(Oddel, Machines_id, Aktivnost_id, Frekfentnost, Data, Operator):
    link=psy.connect("dbname='forumdb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("INSERT INTO Machine_Activity VALUES (%s,%s,%s,%s,%s,%s)", (Oddel, Machines_id, Aktivnost_id, Frekfentnost, Data, Operator))
    link.commit()
    link.close()

record_keep('Pletilici', 1, 1, 15, '2018-01-02', 'Nikola')
record_keep('Pletilici', 2, 1, 15, '2018-02-11', 'Dragi')
record_keep('Pletilici', 3, 1, 15, '2018-02-09', 'Igor')
record_keep('Pletilici', 4, 1, 15, '2018-01-06', 'Marijan')


def zapisi():
    link =psy.connect("dbname='forumdb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("SELECT * FROM Machine_Activity WHERE CURRENT_DATE - data > frekfentnost")
    rows=cur.fetchall()
    return rows
    link.close()
    
zapisi()




#
# def delete(id):
#     link=psy.connect("Records.db")
#     cur=link.cursor()
#     cur.execute("DELETE FROM Stored WHERE id=?",(id,))
#     link.commit()
#     link.close()
#
# def check():
#     link=psy.connect("Records.db")
#     cur=link.cursor()
#     cur.execute("SELECT * FROM Stored")
#     rows=cur.fetchall()
#     link.close()
#     return rows


# print(check())
