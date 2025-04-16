import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust the path to the parent directory
import pytest
from address_book import AddressBook

@pytest.fixture
def sample_contact_data(): 
    """
    Fixture to provide sample contact data.
    """
    return [
        {
        "first_name": "Aleena",
        "last_name": "Mathews",
        "phone_number": "91 8329392930",
        "address": "123 Street",
        "city": "Cityville",
        "state": "Stateburg",
        "zip": "603203",
        "email": "aleena@gmail.com"
        },
        {
        "first_name": "Aleena",
        "last_name": "Sara",
        "phone_number": "91 8329392930",
        "address": "Abode",
        "city": "Chennai",
        "state": "Tamil Nade",
        "zip": "602930",
        "email": "aleena@gmail.com"
        }
    ]

@pytest.fixture
def sample_contact_book():
    return AddressBook("contacts")

def test_add_valid_contact(sample_contact_data,sample_contact_book): 
    """
    Test function to add a valid contact.
    """
    for data in sample_contact_data:
        sample_contact_book.add_contact(**data)  # adding contacts to address book
    
    for contact in sample_contact_book.contacts:
        print(contact)

    assert len(sample_contact_book.contacts) == 2 # checking if contact is added
    assert sample_contact_book.contacts[0].first_name == "Aleena"
    assert sample_contact_book.contacts[1].last_name == "Sara"

def test_add_invalid_contact(sample_contact_book):
    """
    Test function to add an invalid contact.
    """
    sample_contact_book = AddressBook("contact")
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
        sample_contact_book.add_contact(**invalid_contact)

    assert len(sample_contact_book.contacts) == 0  # checking that no contacts were added

def test_edit_contact(sample_contact_data,sample_contact_book):
    """
    Test function to edit details
    """
    for data in sample_contact_data:
        sample_contact_book.add_contact(**data)
    
    sample_contact_book.edit_contact("Aleena","email","amgmail.com","Sara")
    assert sample_contact_book.contacts[1].email == "am@gmail.com"
    

