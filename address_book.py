from contacts import Contact

class AddressBook:
    def __init__(self,address_book_name):
        self.address_book_name = address_book_name
        self.contacts = []

    def add_contact(self,first_name,last_name,phone_number,address,city,state,zip,email):
        contact = Contact(first_name,last_name,phone_number,address,city,state,zip,email)
        self.contacts.append(contact)
