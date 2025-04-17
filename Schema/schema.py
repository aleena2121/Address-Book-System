from pydantic.dataclasses import dataclass
from typing import get_type_hints

@dataclass
class ContactSchema:  # schema for contact class
    first_name : str
    last_name : str
    email : str
    phone_number : str
    address : str
    state : str
    city : str
    zip : str

def get_contact_details(schema_cls):
    """
    Fucntion to get input from user
    """
    field_names = get_type_hints(schema_cls).keys()
    input_data = {}

    for field in field_names:
        value = input(f"{field.replace('_', ' ').title()}: ").strip()
        input_data[field] = value

    return schema_cls(**input_data)