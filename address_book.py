from contacts import Contact
import re

def validate_contact(func):  # decorator function to validate contact details
    def wrapper(*args, **kwargs):
        if not re.match(r"^[A-Za-z]{2,}$", kwargs['first_name']):
            raise ValueError("\nFirst name must contain only letters and be at least 2 characters long.")

        if not re.match(r"^[A-Za-z]{2,}$", kwargs['last_name']):
            raise ValueError("\nLast name must contain only letters and be at least 2 characters long.")

        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", kwargs['email']):
            raise ValueError("\nInvalid email format.")

        if not re.match(r"(\+?[\d\s]{1,6})?\d{10}$", kwargs['phone_number']):
            raise ValueError("\nPhone number must be 10 to 12 digits long.")

        return func(*args, **kwargs)
    return wrapper

class AddressBook:
    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.contacts = []

    @validate_contact
    def add_contact(self, **kwargs): # adding contact to address book
        contact = Contact(
            kwargs["first_name"],
            kwargs["last_name"],
            kwargs["phone_number"],
            kwargs["address"],
            kwargs["city"],
            kwargs["state"],
            kwargs["zip"],
            kwargs["email"]
        )
        self.contacts.append(contact)
        print("Contact added successfully.")