import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import get_type_hints
from Schema import schema
import json
from Database import connection


def load_contacts_from_json(filename, batch_size):   # inserting data from json in batches
    columns = list(get_type_hints(schema.ContactSchema).keys())
    columns.append('address_book_id')

    def call_add_contact(cursor, **kwargs):
        args = [kwargs[col] for col in columns]
        cursor.callproc('add_contacts_to_db', args)  # calling stored procedures

    conn = connection.connect_db()
    cursor = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        contacts = json.load(file)

    total = len(contacts)
    batch = []
    count = 0

    for contact in contacts:
        batch.append(contact)

        if len(batch) >= batch_size:
            for c in batch:
                call_add_contact(cursor, **c)
            conn.commit()
            count += len(batch)
            print(f"Inserted {count}/{total} records")
            batch.clear()

    if batch:
        for c in batch:
            call_add_contact(cursor, **c)
        conn.commit()
        count += len(batch)
        print(f"Inserted {count}/{total} records")

    cursor.close()
    conn.close()

    print("All contacts inserted successfully!")

if __name__ == "__main__":
    load_contacts_from_json()