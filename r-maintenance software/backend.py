from datetime import date
import psycopg2 as psy

link = psy.connect("dbname=maintenancedb", user="postgres", password="post", host="localhost", port="5432")
cur = link.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS LOGS (ID INTEGER, Oddel TEXT, Broj INTEGER, Opis TEXT, Data DATE, Status TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS WORKING (ID INTEGER, Oddel TEXT, Broj INTEGER, Opis TEXT, Data DATE, Status TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS TEMP (ID INTEGER, Oddel TEXT, Broj INTEGER, Opis TEXT, Data DATE, Status TEXT)")
link.commit()
link.close()

def save_temp_log(oddel, broj, note, date, id=None): #datestart datefinish) oddel, broj, opis, date=None, operator, status=None, ID=None
    # date = date.today()
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("INSERT INTO TEMP VALUES(%s,%s,%s,%s %s)",(oddel, broj, note, date, id))
    link.commit()
    link.close()

def started_working(status):
    link = psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("UPDATE WORKING SET STATUS=Active")
    link.commit()
    link.close()

def view_temp_logs():
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("FROM TEMP SELECT *")
    link.commit()
    link.close()

def save_log(oddel, broj, note, date=None, id=None): #date started = date from temp log, date = date finished
    # date = date.today()
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("INSERT INTO LOGS VALUES(%s,%s,%s,%s,%s)",(id, oddel, broj, note, date))
    link.commit()
    link.close()

# save_log("Pletilici", 1, "Problem so edna glava")

def view_saved_logs():
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("SELECT * FROM LOGS")
    link.commit()
    link.close()

def filter_logs(startdate=None, enddate=None, id=None, Broj=None): #moze ke ima plus filteri ke vidime. Filtriranje po mashina treba da ima isto taka ..
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("SELECT FROM LOGS WHERE Data BETWEEN %s AND %s")
    link.commit()
    link.close()

# MAYBE ADD Filtering by date later... not .. dont make it more complex than it needs to be. or maybe you are gonna have to have this .. fck me... ...
