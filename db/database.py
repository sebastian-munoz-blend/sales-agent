import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect("ventas.db")
    df = pd.read_csv("data/ventas.csv")
    df.to_sql("ventas", conn, if_exists="replace", index=False)
    conn.close()
    print("Base de datos creada ✅")

def get_connection():
    return sqlite3.connect("ventas.db")