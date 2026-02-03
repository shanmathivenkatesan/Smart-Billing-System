import sqlite3

def get_db():
    conn = sqlite3.connect("aiag03.db")
    return conn
