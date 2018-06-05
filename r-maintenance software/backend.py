from datetime import date
import psycopg2 as psy

link = psy.connect("dbname=maintenancedb", user="postgres", password="post", host="localhost", port="5432")
cur = link.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS LOGS (Oddel TEXT, Broj INTEGER, Opis TEXT, Data INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS TEMP (Oddel TEXT, Broj INTEGER, Opis TEXT, Data INTEGER)")
link.commit()
link.close()

def save_temp_log(oddel, broj, note, date=None):
    # date = date.today()
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("INSERT INTO TEMP VALUES(%s,%s,%s,%s)",(oddel, broj, note, date))
    link.commit()
    link.close()

def view_temp_logs():
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("FROM TEMP SELECT *")
    link.commit()
    link.close()

def save_log(oddel, broj, note, date=None):
    # date = date.today()
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("INSERT INTO LOGS VALUES(%s,%s,%s,%s)",(oddel, broj, note, date))
    link.commit()
    link.close()

save_log("Pletilici", 1, "asdasdasd")

def view_saved_logs():
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("FROM LOGS SELECT *")
    link.commit()
    link.close()

# MAYBE ADD Filtering by date later... not .. dont make it more complex than it needs to be. or maybe you are gonna have to have this .. fck me... ...
