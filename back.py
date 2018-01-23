from tkinter import *
import csv
import datetime

def zapis():
    f = open('database.csv', 'w')
    z = str(datetime.datetime.now())
    f.write(z)
    print(z)
    f.close()
