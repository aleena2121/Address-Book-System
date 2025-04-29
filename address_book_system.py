import mysql
from address_book import AddressBook
from Operations import queries

class AddressBookSystem:
    def __init__(self):
        self.address_books = {}  # Dictionary to store multiple address books

    def get_address_book(self, name):
        """
        Function to get address book
        """
        if name in self.address_books: 
            return self.address_books[name]
        if name in queries.get_all_address_books():
            self.address_books[name] = AddressBook(name)
            return self.address_books[name]
        raise ValueError(f"Address book '{name}' does not exist.")

    def add_address_book(self,name):
        """
        Function to create a new address book
        """
        try:
            if queries.get_address_book_id(name) is not None:
                self.address_books[name] = AddressBook(name)
                print(f"Address Book '{name}' already exists in database.")
                return
            
            queries.create_and_insert('address_book', name=name)
            self.address_books[name] = AddressBook(name)
            print(f"\nSuccessfully created Address Book - {name}")
        except mysql.connector.Error as db_err:
            print(f"Database error while creating address book: {db_err}")
        except Exception as err:
            print(f"Unexpected error: {err}")

    def get_all_address_books(self):
        """
        To get all address books
        """
        results = queries.get_all_address_books()
        return results
    
    def delete_address_book(self,name):
        """
        To delete an address book by name
        """
        queries.delete_from_table("address_book",name=name)
        self.address_books.pop(name, None)
        print(f"\nSuccessfully Deleted Address Book - {name}")