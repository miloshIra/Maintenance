import sqlite3
import pandas as p
import datetime

def link():
    link =sqlite3.connect("records.db")
    df = p.read_sql_query("CREATE TABLE IF NOT EXISTS Stored (id INTEGER PRIMARY KEY, Oddel text, Mashina text, Aktivnost text, Data text, Operatori text  )", link)
    print(df)
link()
