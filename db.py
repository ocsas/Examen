# db.py
import sqlite3

DB_PATH = "alumnos.db"

def get_db():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con

def row_to_dict(row):
    return dict(row) if row else None
import sqlite3

DB_PATH = "alumnos.db"

def get_db():
   
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con

def row_to_dict(row):
  
    return dict(row) if row else None
