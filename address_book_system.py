from address_book import AddressBook

class AddressBookSystem:
    def __init__(self):
        self.address_books = {}  # Dictionary to store multiple address books

    def get_address_book(self, name):
        if name in self.address_books: 
            return self.address_books[name]
        raise ValueError(f"Address book '{name}' does not exist.")

    def add_address_book(self,name):
        self.address_books[name] = AddressBook(name)
        print(f"\nSuccessfully created Address Book - {name}")

    def get_all_address_books(self):
        return self.address_books