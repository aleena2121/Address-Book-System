import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust the path to the parent directory
import pytest
from address_book import AddressBook
from address_book_system import AddressBookSystem
from search_contacts import SearchContacts
from main import AddressBookMain

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
        "city": "Gurugram",
        "state": "Haryana",
        "zip": "122022",
        "email": "aleena@gmail.com"
        },
        {
        "first_name": "Aleena",
        "last_name": "Sara",
        "phone_number": "91 8329392930",
        "address": "345 Street",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "zip": "602930",
        "email": "aleena@gmail.com"
        }
    ]

@pytest.fixture
def sample_contact_book():
    """
    Fixture to create address book object
    """
    return AddressBook("contacts")

def test_add_multiple_address_books():
    """
    Test function to add multiple address books"""
    ab = AddressBookSystem()
    ab.add_address_book("Personal")
    ab.add_address_book("Work")
    assert len(ab.address_books) == 2

def test_add_valid_contact(sample_contact_data,sample_contact_book): 
    """
    Test function to add a valid contact.
    """
    sample_contact_book.add_contact(**sample_contact_data[0])  # adding contacts to address book
    
    for contact in sample_contact_book.contacts:
        print(contact)

    assert len(sample_contact_book.contacts) == 1 # checking if contact is added
    assert sample_contact_book.contacts[0].first_name == "Aleena"
    assert sample_contact_book.contacts[0].last_name == "Mathews"

def test_add_multiple_valid_contacts(sample_contact_data,sample_contact_book): 
    """
    Test function to add multiple valid contact.
    """
    for data in sample_contact_data:
        sample_contact_book.add_contact(**data)  # adding contacts to address book
    
    for contact in sample_contact_book.contacts:
        print(contact)

    assert len(sample_contact_book.contacts) == 2 # checking if contact is added
    assert sample_contact_book.contacts[0].first_name == "Aleena"
    assert sample_contact_book.contacts[1].last_name == "Sara"

def test_add_duplicate_contact(sample_contact_book,sample_contact_data):
    """
    Test function to avoid adding duplicate name contacts"""
    sample_contact_book.add_contact(**sample_contact_data[0])
    contact2 = {
        "first_name": "Aleena",
        "last_name": "Mathews",  # contact with same first name and last name already added
        "phone_number": "91 8329392930",
        "address": "345 Street",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "zip": "602930",
        "email": "aleena@gmail.com"
        }
    sample_contact_book.add_contact(**contact2)

    assert len(sample_contact_book.contacts) == 1  # 2 == 1 as duplicate contact will not be added


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
    
    sample_contact_book.edit_contact("Aleena","email","am@gmail.com","Sara")
    assert sample_contact_book.contacts[1].email == "am@gmail.com"

def test_invalid_edit_contact(sample_contact_data,sample_contact_book):
    """
    Test function to edit details
    """
    for data in sample_contact_data:
        sample_contact_book.add_contact(**data)

    with pytest.raises(ValueError):
        sample_contact_book.edit_contact(first_name="Aleena",field="email",email="amgmail.com",last_name="Sara")
    assert sample_contact_book.contacts[1].email != "amgmail.com"

def test_delete_contact(sample_contact_book,sample_contact_data):
    """
    Test function to delete data
    """
    for data in sample_contact_data:
        sample_contact_book.add_contact(**data)

    sample_contact_book.delete_contact("Aleena","Sara")
    assert len(sample_contact_book.contacts) == 1

def test_search_all_address_books(sample_contact_data,sample_contact_book):
    """
    Test Function to search accross all address books by city or state
    """
    for data in sample_contact_data:
        sample_contact_book.add_contact(**data)
    
    searcher = SearchContacts()
    AddressBookMain.system.address_books["TestBook"] = sample_contact_book
    searcher.address_books = AddressBookMain.get_all_address_books()
    results_by_city = searcher.search_in_all_address_books_by_city("Chennai") 
    results_by_state  = searcher.search_in_all_address_books_by_state("Haryana") 
    assert len(results_by_city) == 1
    assert len(results_by_state) == 1

def test_add_to_dictionary_by_city_and_state(sample_contact_book,sample_contact_data):
    """
    Test function to check if dictionary is maintained by city and state
    """
    for data in sample_contact_data:
        sample_contact_book.add_contact(**data)
    
    assert len(sample_contact_book.people_in_city) == 2

def test_save_to_txt_file(sample_contact_book,sample_contact_data):
    """
    Test function to check if contacts are saved in txt file
    """
    for data in sample_contact_data:
        sample_contact_book.add_contact(**data)
    
    sample_contact_book.save_to_text_file("file.txt")

    with open("file.txt","r") as file: 
        content = file.read()  # reading file content
    
    assert "Aleena" in content  # checking if contact is added to file or not