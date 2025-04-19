from address_book_system import AddressBookSystem

class SearchContacts(AddressBookSystem):
    def __init__(self):
        super().__init__()
        self.address_books = {}

    def search_in_all_address_books_by_city(self, city):
        """
        Searches contacts by city accross all address books
        """
        search_results = []
        for name, address_book in self.address_books.items():
            for key,contact in address_book.people_in_city.items():
                if key.lower() == city.lower():
                    if isinstance(contact, list):
                        search_results.extend(contact)
                    else:
                        search_results.append(contact)

        return search_results
    
    def search_in_all_address_books_by_state(self, state):
        """
        Searches contacts by city accross all address books
        """
        search_results = []
        for name, address_book in self.address_books.items():
            for key,contact in address_book.people_in_state.items():
                if key.lower() == state.lower():
                    if isinstance(contact, list):
                        search_results.extend(contact)
                    else:
                        search_results.append(contact)

        return search_results