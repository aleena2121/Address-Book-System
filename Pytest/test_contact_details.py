import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust the path to the parent directory
import pytest
from address_book import AddressBook
from address_book import validate_contact

@pytest.fixture
def sample_contact_data(): 
    """
    Fixture to provide sample contact data.
    """
    return {
        "first_name": "Aleena",
        "last_name": "Mathews",
        "phone_number": "91 8329392930",
        "address": "123 Street",
        "city": "Cityville",
        "state": "Stateburg",
        "zip": "12345",
        "email": "aleena@gmail.com"
    }

def test_add_valid_contact(sample_contact_data): 
    """
    Test function to add a valid contact.
    """
    ab = AddressBook("contact")
    ab.add_contact(**sample_contact_data)

    assert len(ab.contacts) == 1
    assert ab.contacts[0].first_name == "Aleena"

def test_add_invalid_contact():
    """
    Test function to add an invalid contact.
    """
    ab = AddressBook("contact")
    invalid_contact = {
        "first_name": "Bob",
        "last_name": "Smith",
        "phone_number": "invalid", # invalid phone number
        "address": "123 Street",
        "city": "Cityville",
        "state": "Stateburg",
        "zip": "12345",
        "email": "bob@example.com"
    }

    with pytest.raises(ValueError):  # ValueError expected
        ab.add_contact(**invalid_contact)

    assert len(ab.contacts) == 0  # checking that no contacts were added