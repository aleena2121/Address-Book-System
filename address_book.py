from Utils import validate_contact
from contacts import Contact
import re

class AddressBook:
    def __init__(self, address_book_name):
        """
        Instanciates an address book object
        
        Args:
        address_book_name: name of the address book
        """
        self.address_book_name = address_book_name
        self.contacts = []
        self.people_in_city = {}
        self.people_in_state = {}

    @validate_contact.validate_contact
    def add_contact(self, **kwargs):
        """
        Function to add contact details to address boook
        
        Args:
        **kwargs: Contact details
        """

        contact = Contact(**kwargs)
        available_contacts = self.find_contact(contact.first_name)
        if [contact.first_name,contact.last_name] in available_contacts:
            print(f"Contact with same name already exists!")
            return
        self.contacts.append(contact)
        if contact.city not in self.people_in_city:  # adding contact object to dictionary corresponding to city
            self.people_in_city[contact.city] = [] 
        self.people_in_city[contact.city].append(contact)
        if contact.state not in self.people_in_state:   # adding contact object to dictionary corresponding to state
            self.people_in_state[contact.state] = []
        self.people_in_state[contact.state].append(contact)
        print("\nContact added successfully.")
    

    @validate_contact.validate_contact
    def edit_contact(self, first_name, field=None, new_value=None, last_name_=None, **kwargs):
        """
        Function to edit details for contact
        
        Args:
        first_name: first name of contact to edit
        field: field to be editted
        new_value: new value to be addes
        last_name: last name of contact to be edited, if there exists multiple people with same first name
        kwargs: passing field, new value pair
        """
        edit_kwargs = kwargs.copy()
        if field and new_value:
            edit_kwargs[field] = new_value
        
        for contact in self.contacts:
            if contact.first_name == first_name:
                if last_name_ is not None:
                    if contact.last_name != last_name_:
                        continue
                
                for attr, value in edit_kwargs.items():
                    setattr(contact, attr, value)   # editing the values
                print("Contact edited!")
                return
        
        print("Contact not found")

    
    def find_contact(self,first_name):  
        """
        Function to get a list of all contacts with same first name

        Args:
        first_name: first name of contact to find

        Returns:
        available_contacts: list of contacts found
        """
        available_contacts = []
        for contact in self.contacts:
            if contact.first_name == first_name:
                available_contacts.append([contact.first_name,contact.last_name])
        return available_contacts

    def delete_contact(self,first_name,last_name=None):
        """
        Function to delete a contact from the address book using first name and last name

        Args:
        first_name: name of contact to be deletes
        last_name(optional): last name of contact to be deleted, if there exists multiple people with same first name
        """
        for contact in self.contacts:
            if contact.first_name == first_name:
                if last_name is not None:
                    if contact.last_name == last_name:
                        self.contacts.remove(contact)
                        print("Contact deleted!")
                        return
                else:
                    self.contacts.remove(contact)
                    print("Contact deleted!")
                    return
        print("Contact not found")
