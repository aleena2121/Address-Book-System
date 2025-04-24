import mysql.connector
from config.db_config import db_config

def create_database():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS AddressBookDB")
        print("Database created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
