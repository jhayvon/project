import sqlite3 as sql

def connection():
    conn = sql.connect("tourist.db")
    return conn