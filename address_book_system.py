from address_book import AddressBook

class AddressBookSystem:
    def __init__(self):
        self.address_books = {}  # Dictionary to store multiple address books

    def get_address_book(self, name):
        if name not in self.address_books:  # creates new address if not exists
            self.address_books[name] = AddressBook(name)
        return self.address_books[name]
