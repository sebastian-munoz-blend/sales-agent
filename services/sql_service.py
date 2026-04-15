from db.database import get_connection
import pandas as pd

def execute_query(query: str):
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df