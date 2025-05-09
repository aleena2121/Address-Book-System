from pydantic.dataclasses import dataclass
from typing import get_type_hints

@dataclass
class ContactSchema:  # schema for contact class
    first_name : str
    last_name : str
    email : str
    phone_number : str
    address : str
    city : str
    state : str
    zip : str

def get_contact_details(schema_cls):
    """
    Function to get input from user
    """
    field_names = get_type_hints(schema_cls).keys()
    input_data = {field : input(f"{field.replace('_', ' ').title()}: ").strip() for field in field_names}

    return schema_cls(**input_data)