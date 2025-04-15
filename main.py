from address_book import AddressBook

class AddressBookMain:
    @staticmethod
    def start():  # addressing the user
        print("\nWelcome to the Address Book Program!")

    @staticmethod
    def menu():  # menu for user to select options
        print(f"\nMenu:\n1. Add new Contact\n2. Display Contacts\n3. Exit") # menu options
        try:
            option = int(input("Enter option: "))
            match option:
                case 1:  # add new contact
                    details = {}
                    print("\nEnter contact details:")
                    details["first_name"] = input("First name: ")
                    details["last_name"] = input("Last name: ")
                    details["email"] = input("Email: ")
                    details["phone_number"] = input("Phone number: ")
                    details["address"] = input("Address: ")
                    details["city"] = input("City: ")
                    details["state"] = input("State: ")
                    details["zip"] = input("Zip Code: ")
                    address_book_name = input("\nPlease Enter Address Book Name: ") # getting address book name from user
                    try:
                        ab = AddressBook(address_book_name)  # crearing an instance of AddressBook class
                        ab.add_contact(**details)  # adding contact to address book
                    except ValueError as e: 
                        print(e)
                
                case 2:
                    pass

                case 3: # to exit the program
                    exit()  
        except ValueError:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    AddressBookMain.start() # starting the program using the static method
    while True:
        AddressBookMain.menu()  # displaying the menu options and taking user input
