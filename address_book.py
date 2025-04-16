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
            raise ValueError("\nPhone number must be 10 digits long and can have a country code.")
        
        if not re.match(r"^\d{6}$",kwargs['zip']):
            raise ValueError("\nZip code can be only 6 digits long")
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
        print("\nContact added successfully.")
    
    def edit_contact(self, first_name, field, new_value, last_name=None):
        for contact in self.contacts:
            if contact.first_name == first_name:
                if last_name is not None:
                    if contact.last_name == last_name:
                        setattr(contact, field, new_value)
                        print("Contact edited!")
                        return
                else:
                    setattr(contact, field, new_value)
                    print("Contact edited!")
                    return
        print("Contact not found")

    
    def find_contact(self,first_name):
        available_contacts = []
        for contact in self.contacts:
            if contact.first_name == first_name:
                available_contacts.append([contact.first_name,contact.last_name])
        return available_contacts