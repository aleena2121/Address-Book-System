from address_book import AddressBook
from address_book_system import AddressBookSystem
from Schema import schema
from datetime import datetime

class AddressBookMain:
    system = AddressBookSystem()  # Use AddressBookSystem to manage all address books

    @staticmethod
    def start():
        """
        static method to greet the user
        """
        print("\nWelcome to the Address Book Program!")

    @staticmethod
    def menu():
        """
        Function to get the menu option input from user
        """
        print("\nMenu:\n1. Add new Contact\n2. Display Contacts\n3. Edit Contact\n4. Delete Contact\n5. Add new Address Book\n6. Display all Address Books\n7. Delete Address Book\n8. Search by City\n9. Search by State\n10. Sort by Location\n11. Save Contacts to File\n12. Read Contacts from a File\n0. Exit")  # menu options for user
        try:
            option = int(input("Enter option: "))
            if option == 1:
                AddressBookMain.add_contact()
            elif option == 2:
                AddressBookMain.display_contacts()
            elif option == 3:
                AddressBookMain.edit_contact()
            elif option == 4:
                AddressBookMain.delete_contact()
            elif option == 5:
                AddressBookMain.add_address_book()
            elif option == 6:
                AddressBookMain.get_all_address_books()
            elif option == 7:
                AddressBookMain.delete_address_book()
            elif option == 8:
                AddressBookMain.search_all_address_books_by_city()
            elif option == 9:
                AddressBookMain.search_all_address_books_by_state()
            elif option == 10:
                AddressBookMain.sort_by_location()
            elif option == 11:
                AddressBookMain.save_to_file()
            elif option == 12:
                AddressBookMain.read_contacts_from_file()
            elif option == 0:  # exits the program
                print("\nGoodbye!\n")
                exit()
            else:
                print("Invalid option")
        except ValueError as e:
            print(e)

    @staticmethod
    def add_contact():
        """
        Function to get input from user to add contact and to add it in address book
        """
        books = AddressBookMain.get_all_address_books()
        if not books:  # if no address book exists ask user to create one
            print("\nCreate an address book to continue.")
            return

        name = input("\nPlease enter Address Book Name to add contact in: ")
        try:
            ab = AddressBookMain.system.get_address_book(name)
            details = schema.get_contact_details(schema.ContactSchema)
            ab.add_contact(**details.__dict__)
        except ValueError as e:
            print(e)


    @staticmethod
    def display_contacts():
        """
        Fucntion to display all contacts in an address book
        """
        books = AddressBookMain.get_all_address_books()
        if not books:  # if no address book exists ask user to create one
            print("\nCreate an address book to continue.")
            return
        
        name = input("\nEnter Address Book Name to display contacts from: ")
        ab = AddressBookMain.system.get_address_book(name)
        if ab.contacts:
            sorted_contacts = sorted(ab.contacts, key=lambda c: c.first_name.lower())  # sort all contacts alphabetically
            print(f"\nContacts in {ab.address_book_name}: ")
            for contact in sorted_contacts:
                print(contact)
        else:
            print("No contacts found.")

    @staticmethod
    def edit_contact():
        """
        Function to get input from user to edit contact and edit it correspondingly in address book
        """
        books = AddressBookMain.get_all_address_books()
        if not books:  # if no address book exists ask user to create one
            print("\nCreate an address book to continue.")
            return

        name = input("\nPlease enter Address Book Name where you want to edit the contact: ")
        ab = AddressBookMain.system.get_address_book(name)

        first_name = input("Enter first name of the contact you want to edit: ")
        available_contacts = ab.find_contact(first_name)
        
        if len(available_contacts) == 0:
            print("No contacts found")
            return
            
        if len(available_contacts) == 1:
            last_name = available_contacts[0][1]
        else:
            print("Which one of these contacts you want to edit?:")
            for i, contact in enumerate(available_contacts, 1):
                print(f"{i}. {contact[0]} {contact[1]}")
            choice = int(input("\nEnter the contact number: ")) - 1
            last_name = available_contacts[choice][1]

        print("\nEnter the detail you want to edit:")
        print("1. First Name\n2. Last Name\n3. Email\n4. Phone Number\n5. Address\n6. City\n7. State\n8. Zip Code\n9. Cancel")
        
        try:
            option = int(input("Enter option: "))
            if option == 9:
                print("Edit cancelled.")
                return
                
            fields = ["first_name", "last_name", "email", "phone_number","address", "city", "state", "zip"]
            field = fields[option - 1]
            new_value = input("Enter new value: ")
            
            try:
                ab.edit_contact(
                    first_name=first_name,
                    last_name_=last_name,
                    **{field: new_value}  # Pass as kwargs to trigger validation
                )
            except ValueError as e:
                print(f"Validation error: {e}")
                
        except ValueError:
            print("Invalid input. Edit cancelled.")

    @staticmethod
    def delete_contact():
        """
        Function to get input to delete contact 
        """
        books = AddressBookMain.get_all_address_books()
        if not books:
            print("\nCreate an address book to continue.")
            return
        name = input("\nPlease enter Address Book Name where you want to delete the contact: ")
        ab = AddressBookMain.system.get_address_book(name)
        first_name = input("\nEnter first name of the contact you want to delete: ")
        available_contacts = ab.find_contact(first_name)

        if len(available_contacts) == 1:
            ab.delete_contact(first_name=first_name)

        elif len(available_contacts) > 1:  # if more than one contact with same first name exists
            print("\nWhich one of these contacts you want to delete?: ")
            for i in range(len(available_contacts)):
                print(f"{i+1}. {available_contacts[i][0]} {available_contacts[i][1]}")  # printing the contacts with same first name
            contact = int(input("\nEnter the contact you want to delete from the above list: "))
            ab.delete_contact(first_name=first_name,last_name=available_contacts[contact-1][1])

    @staticmethod
    def add_address_book():
        """
        Function to add a new address book
        """
        address_book_name = input("Enter name for address book: ")
        AddressBookMain.system.add_address_book(address_book_name)
    
    @staticmethod
    def delete_address_book():
        """
        
        """
        books = AddressBookMain.get_all_address_books()
        if not books:
            print("\nCreate an address book to continue.")
            return
        address_book_name = input("\nEnter name of address book to delete: ")
        AddressBookMain.system.delete_address_book(address_book_name)

    @staticmethod
    def get_all_address_books():
        """
        Function to get all address books
        """
        books = AddressBookMain.system.get_all_address_books()
        if books:
            print(f"\nAddress Books - ")
            for i, book_name in enumerate(books.keys(), 1):
                print(f"{i}. {book_name}")
            return books
        else:
            print("\nNo Address Book found")

    @staticmethod
    def search_all_address_books_by_city():
        """
        Function to search by city accross all address books
        """
        from search_contacts import SearchContacts
        books = AddressBookMain.get_all_address_books()
        if not books:
            print("\nCreate an address book to continue.")
            return
        
        city = input("\nEnter city to search contacts: ")
        searcher = SearchContacts()  # creating an object of search class
        searcher.address_books = AddressBookMain.system.get_all_address_books()  # passing all address books to search object
        results = searcher.search_in_all_address_books_by_city(city)
        results = sorted(results, key=lambda c: c.first_name.lower())  # sort search results aphabetically
        if results:
            print("\nSearch Results:")
            print(f"{len(results)} contacts found")
            for i,contact in enumerate(results,1):
                print(f"{i}. {contact}")
        else:
            print(f"\nNo contacts found in {city}.")
    
    @staticmethod
    def search_all_address_books_by_state():
        """
        Function to search by state accross all address books
        """
        from search_contacts import SearchContacts
        books = AddressBookMain.get_all_address_books()
        if not books:
            print("\nCreate an address book to continue.")
            return
        
        state = input("\nEnter state to search contacts: ")
        searcher = SearchContacts()  # creating an object of search class
        searcher.address_books = AddressBookMain.system.get_all_address_books()  # passing all address books to search object
        results = searcher.search_in_all_address_books_by_state(state)
        results = sorted(results, key=lambda c: c.first_name.lower())  # sort search results aphabetically
        if results:
            print("\nSearch Results:")
            print(f"\n{len(results)} contacts found")
            for i,contact in enumerate(results,1):
                print(f"{i}. {contact}")
        else:
            print(f"\nNo contacts found in {state}.")

    
    @staticmethod
    def sort_by_location():
        """
        Function to sort contacts by city, state, or zip in a selected or all address books
        """
        books = AddressBookMain.system.get_all_address_books()
        if not books:
            print("\nCreate an address book to continue.")
            return

        print("\nSelect an Address Book:")
        print("0. All Address Books") # to sort contacts in all the address books
        book_list = list(books.keys())
        for i, book_name in enumerate(book_list, 1):
            print(f"{i}. {book_name}")

        choice = int(input("Enter your choice: "))  # to sort through a particular address book
        selected_books = book_list if choice == 0 else [book_list[choice - 1]]

        print("\nSort by:\n1. City\n2. State\n3. Zip Code")
        sort_choice = int(input("Enter your choice: "))
        sort_key = ['city', 'state', 'zip'][sort_choice - 1]

        all_contacts = []
        for book_name in selected_books:
            book = books[book_name]
            all_contacts.extend(book.contacts)

        if not all_contacts:
            print("No contacts found.")
            return

        sorted_contacts = sorted(all_contacts, key=lambda c: getattr(c, sort_key))  # sorting according to input provided
        print(f"\nSorted Contacts by {sort_key.title()}:")
        for contact in sorted_contacts:
            print(contact)
    
    @staticmethod
    def save_to_file():
        books = AddressBookMain.system.get_all_address_books()
        if not books:
            print("\nCreate an address book to continue.")
            return

        print("\nSelect option to save file: \n1. Text File\n2. CSV File")
        save_file_to = int(input("\nEnter Choice: "))
        print("\nSelect an Address Book:")
        print("0. All Address Books") # to sort contacts in all the address books
        book_list = list(books.keys())
        for i, book_name in enumerate(book_list, 1):
            print(f"{i}. {book_name}")

        choice = int(input("\nEnter your choice: "))  # to sort through a particular address book
        selected_books = book_list if choice == 0 else [book_list[choice - 1]]

        if save_file_to == 1:   # save to .txt file
            for book_name in selected_books:
                filename = f"{book_name}.txt"
                address_book = books[book_name]
                address_book.save_to_text_file(filename)
        
        elif save_file_to == 2:  # save to csv file
            for book_name in selected_books:
                filename = f"{book_name}.csv"
                address_book = books[book_name]
                address_book.save_to_csv_file(filename)
        
    @staticmethod
    def read_contacts_from_file():
        """
        Function to read contacts from a file
        """
        books = AddressBookMain.system.get_all_address_books()
        if not books:
            print("\nCreate an address book to continue.")
            return

        file_name = input("\nEnter file name to read: ")

        try:
            print(f"\nContent in {file_name}:")
            with open(file_name,"r") as file:
                contacts = file.readlines()
        except FileNotFoundError:
            print("\nFile not found, Try again")
        
        for contact in contacts:
            print(contact)
        
if __name__ == "__main__":
    AddressBookMain.start() # starting the program using the static method
    while True:
        AddressBookMain.menu()  # displaying the menu options and taking user input