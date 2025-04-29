import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import get_type_hints
from faker import Faker
from Schema import schema
from contacts import Contact
from Utils import validate_contact
import json_to_db
import json
fake = Faker()


file_path = "Generate_Data\contacts.json"

def insert_data_to_json():
    valid_contacts = []
    columns = list(get_type_hints(schema.ContactSchema).keys())
    columns.append('address_book_id')

    for _ in range(100):
        contact = [fake.first_name(),fake.last_name(),fake.email(),f"{fake.random_int(min=10, max=99)} {fake.msisdn()[0:10]}",fake.address(),fake.city(),fake.state(),fake.zipcode(),fake.random.choice([11,12,13])]
        columns = list(get_type_hints(schema.ContactSchema).keys())
        columns.append('address_book_id')
        details = dict(zip(columns, contact))
        if validate_contact.validate_contact(details):
            valid_contacts.append(details)
        else:
            print(f"Invalid contact skipped: {details}")

    with open(file_path, 'w') as file:
        json.dump(valid_contacts, file, indent=4)

if __name__ == "__main__":
    insert_data_to_json()
    json_to_db.load_contacts_from_json(filename=file_path,batch_size=1000)