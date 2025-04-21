from address_book import AddressBook

class AddressBookSystem:
    def __init__(self):
        self.address_books = {}  # Dictionary to store multiple address books

    def get_address_book(self, name):
        """
        Function to get address book
        """
        if name in self.address_books: 
            return self.address_books[name]
        raise ValueError(f"Address book '{name}' does not exist.")

    def add_address_book(self,name):
        """
        Function to create a new address book
        """
        self.address_books[name] = AddressBook(name)
        print(f"\nSuccessfully created Address Book - {name}")

    def get_all_address_books(self):
        """
        To get all address books
        """
        return self.address_books
    
    def delete_address_book(self,name):
        """
        To delete an address book by name
        """
        self.address_books.pop(name, None)
        print(f"\nSuccessfully Deleted Address Book - {name}")