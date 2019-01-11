import datetime
import psycopg2 as psy


link = psy.connect("dbname=maintenancedb", user="postgres", password="post", host="localhost", port="5432")
cur = link.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS LOGS (ID SERIAL, Oddel TEXT, Broj TEXT, Opis TEXT, OPERATOR TEXT, Status TEXT, Data TIMESTAMP, MECH TEXT)")
#cur.execute("CREATE TABLE IF NOT EXISTS WORKING (Oddel TEXT, Broj TEXT, Opis TEXT, Data DATETIME, Status TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS TEMPO (ID SERIAL, Oddel TEXT, Broj TEXT, Opis TEXT, OPERATOR TEXT, Status TEXT, Data TIMESTAMP, MECH TEXT, ZAVRSHENO TIMESTAMP, MECHNOTE TEXT)")
link.commit()
link.close()

def save_temp_log(oddel, broj, note, operator, status="Чека", date=None, zavrsheno=None, mech=None, mechNote=None):
     #datestart datefinish) oddel, broj, opis, date=None, operator, status=None, ID=None
    date=(datetime.datetime.now()).strftime('%d-%m-%y %H:%M:%S')  # isto taka treba da ima i avtomatsko id
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("INSERT INTO TEMPO (Oddel, Broj, Opis, Operator, Status, Data) VALUES (%s,%s,%s,%s,%s,%s)",(oddel, broj, note, operator, status, date))
    link.commit()
    link.close()

def started_working(_id, mech):
    link = psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("UPDATE tempo SET mech=%s, status = 'Се работи' WHERE status='Чека' AND id = %s", (mech.get(), _id))
    # cur.execute("UPDATE TEMPO SET mech =%s WHERE ID=%s", [mech], [_id])
    # parametarot mora da e lista ?? wth ?
    # cur.execute("INSERT INTO WORKING SET (%s) WHERE odrzhuvach",(odrzhuvach))
    link.commit()
    link.close()

def finished_working(_id, zavrsheno):
    zavrsheno=(datetime.datetime.now()).strftime('%d-%m-%Y %H:%M:%S')
    link = psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur = link.cursor() # Da se stavi proklet note za mehanicarot sto ja zavrshil
    cur.execute("UPDATE TEMPO SET STATUS = 'Завршено' WHERE STATUS='Се работи' AND ID = %s", [_id])
    link.commit()
    link.close()



def view_temp_logs():
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("SELECT * FROM TEMPO") #WHERE status != 'Завршено'")
    rows=cur.fetchall()
    # link.close()
    return rows

def save_log(oddel, broj, note, date=None, id=None): #date started = date from temp log, date = date finished
    date=(datetime.datetime.now()).strftime('%d-%m-%Y %H:%M:%S')
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("INSERT INTO LOGS VALUES(%s,%s,%s,%s,%s)", ( oddel, broj, note, date, id))
    link.commit()
    link.close()

# save_log("Pletilici", 1, "Problem so edna glava")


def filter_logs(oddel, brojm, odrz): #moze ke ima plus filteri ke vidime. Filtriranje po mashina treba da ima isto taka ..
    link =psy.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
    cur=link.cursor()
    cur.execute("SELECT * FROM TEMPO WHERE oddel=%s OR broj=%s OR mech=%s", oddel.get(), brojm.get(), odrz.get())
    link.commit()
    link.close()


    print(oddel.get())
    print(brojm.get())
    print(pocnato.get())
    print(zavrsheno.get())
    print(odrz.get())


#Raboti prevzemanjeto front to back i obratno .. dodaj note za odrzuvac .. procetno i krano vreme .. i zosto ne raboti querity ffs
