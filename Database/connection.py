import mysql.connector
from config.db_config import db_config

def connect_db():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print("Database connection error:", err)
        return None
