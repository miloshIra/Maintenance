import datetime
import psycopg2 as psy

link = psy.connect("dbname=maintenancedb", user="postgres", password="post", host="localhost", port="5432")
cur = link.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS LOGS ( Oddel TEXT, Broj TEXT, Opis TEXT, Data TEXT, Status TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS WORKING (Oddel TEXT, Broj TEXT, Opis TEXT, Data TEXT, Status TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS TEMPO (Oddel TEXT, Broj TEXT, Opis TEXT, OPERATOR TEXT, Status TEXT, Data TEXT)")
link.commit()
link.close()

def save_temp_log(oddel, broj, note, operator, status="Чека", date=None): #datestart datefinish) oddel, broj, opis, date=None, operator, status=None, ID=None
    date=(datetime.datetime.now()).strftime('%H:%M:%S %d-%m-%Y')        #isto taka treba da ima i avtomatsko id
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("INSERT INTO TEMPO VALUES (%s,%s,%s,%s,%s,%s)",(oddel, broj, note, operator, status, date))
    link.commit()
    link.close()

def started_working():
    link = psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("UPDATE TEMPO SET STATUS = 'Чека' WHERE STATUS='Active'")
    # cur.execute("INSERT INTO WORKING SET (%s) WHERE odrzhuvach",(odrzhuvach))
    link.commit()
    link.close()

def view_temp_logs():
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("SELECT * FROM TEMPO")
    rows=cur.fetchall()
    # link.close()
    return rows

def save_log(oddel, broj, note, date=None, id=None): #date started = date from temp log, date = date finished
    date=(datetime.datetime.now()).strftime('%H:%M:%S %d-%m-%Y')
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("INSERT INTO LOGS VALUES(%s,%s,%s,%s,%s)",(id, oddel, broj, note, date))
    link.commit()
    link.close()

save_log("Pletilici", 1, "Problem so edna glava")

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
