from pydantic.dataclasses import dataclass

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