# from address_book_system import AddressBookSystem

# class SearchContacts(AddressBookSystem):
#     def __init__(self):
#         super().__init__()
#         self.address_books = []
    
#     def search_in_all_address_books(self,city_or_state):
#         search_results = []
#         for address_book in self.get_all_address_books():
#             for contact in address_book.items():
#                 print(contact)
#                 if contact.city == city_or_state or contact.state == city_or_state:
#                     search_results.append(contact)
#         return search_results



from address_book_system import AddressBookSystem

class SearchContacts(AddressBookSystem):
    def __init__(self):
        super().__init__()
        self.address_books = {}

    def search_in_all_address_books(self, city_or_state):
        search_results = []
        for name, address_book in self.address_books.items():
            for contact in address_book.contacts:
                if contact.city.lower() == city_or_state.lower() or contact.state.lower() == city_or_state.lower():
                    search_results.append(contact)
        return search_results
