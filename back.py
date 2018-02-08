import datetime
import pandas as p
import psycopg2 as psy

#IS PANDAS DATAFRAME MUTABLE OR IS IT A TUPPLE !!!!!??!!?!?!?

link =psy.connect("dbname='forumdb' user='postgres' password='post' host='localhost' port='5432'")
cur=link.cursor()
# cur.execute("DROP TABLE Machines")
cur.execute("CREATE TABLE IF NOT EXISTS Machines (Oddel TEXT, Broj INTEGER PRIMARY KEY)")
cur.execute("CREATE TABLE IF NOT EXISTS Activity (id INTEGER PRIMARY KEY, Ime TEXT, Frekfentnost TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Machine_Activity (id INTEGER PRIMARY KEY, Oddel TEXT, Mashina_id INTEGER, Aktivsnot_id INTEGER, Frekfentnost INTEGER, Data TEXT, Operator TEXT)")
link.commit()
link.close()   # Creates a table ako ne postoi ako postoi nisto ... ova ke se brishe izgleda ke ostane samo konekcijata ??



def update(Oddel, Broj):
    link =psy.connect("dbname='forumdb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("INSERT INTO Machines VALUES(%s,%s)",(Oddel, Broj))
    link.commit()
    link.close()


update('Pletilici',1)
update('Pletilici',2)
update('Pletilici',3)
update('Pletilici',5)
update('Pletilici',6)
update('Pletilici',7)
update('Pletilici',8)



# def zapisi():
#     # z = str(datetime.datetime.now())
#     # f = open('database.csv', 'w')
#     # f.write(z)
#     # print(z)
#     link=psy.connect("Records.db")
#     cur=link.cursor()
#     cur.execute("SELECT * FROM Stored")
#     rows=cur.fetchall()
#     link.close()
#     return rows
# zapisi()
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
