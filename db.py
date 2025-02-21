# db.py
import mysql.connector
from config import DB_CONFIG

def get_db_connection():
    connection = mysql.connector.connect(**DB_CONFIG)
    return connection

def query_db(query, args=(), fetchone=False):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, args)
    result = cursor.fetchone() if fetchone else cursor.fetchall()
    conn.close()
    return result

def modify_db(query, args=()):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()
