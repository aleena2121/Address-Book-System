import csv
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Database import connection

def export_to_csv(address_book_name):
    conn = connection.connect_db()
    cursor = conn.cursor()

    cursor.callproc('get_contacts_by_address_book', [address_book_name])  # caling stored procedure to get contacts

    for result in cursor.stored_results():
        rows = result.fetchall()
        headers = [desc[0] for desc in result.description]

    file_name = f"Generate_Data\{address_book_name}_contacts.csv"
    with open(file_name,"w") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    address_book_name = input("Enter address book name: ")
    export_to_csv(address_book_name)