from address_book import AddressBook
from address_book_system import AddressBookSystem

class AddressBookMain:
    system = AddressBookSystem()  # Use AddressBookSystem to manage all address books

    @staticmethod
    def start(): # addressing the user
        print("\nWelcome to the Address Book Program!")

    @staticmethod
    def menu():
        print("\nMenu:\n1. Add new Contact\n2. Display Contacts\n3. Edit Contact\n4. Exit")  # menu options for user
        try:
            option = int(input("Enter option: "))
            if option == 1:
                AddressBookMain.add_contact()
            elif option == 2:
                AddressBookMain.display_contacts()
            elif option == 3:
                AddressBookMain.edit_contact()
            elif option == 4:  # exits the program
                print("Goodbye!")
                exit()
            else:
                print("Invalid option")
        except ValueError:
            print("Please enter a valid number")

    @staticmethod
    def add_contact():
        details = {
            "first_name": input("First name: "),
            "last_name": input("Last name: "),
            "email": input("Email: "),
            "phone_number": input("Phone number: "),
            "address": input("Address: "),
            "city": input("City: "),
            "state": input("State: "),
            "zip": input("Zip Code: ")
        }
        name = input("Please enter Address Book Name: ")  # getting address book name from user
        ab = AddressBookMain.system.get_address_book(name)
        try:
            ab.add_contact(**details)
        except ValueError as e:
            print(e)

    @staticmethod
    def display_contacts():
        name = input("\nEnter Address Book Name to display contacts: ")
        ab = AddressBookMain.system.get_address_book(name)
        if ab.contacts:
            print("\nContacts: ")
            for contact in ab.contacts:
                print(contact)
        else:
            print("No contacts found.")

    @staticmethod
    def edit_contact():
        name = input("Please enter Address Book Name in which you want to edit the contact: ")
        ab = AddressBookMain.system.get_address_book(name)
        if ab:
            first_name = input("Enter first name of the contact you want to edit: ")
            available_contacts = ab.find_contact(first_name)
            if len(available_contacts) == 1:
                if first_name in available_contacts[0]: 
                    print("\nEnter the detail you want to edit:\n1. First Name\n2. Last Name\n3. Email\n4. Phone Number\n5. Address\n6. City\n7. State\n8. Zip Code\n9. Cancel")
                    try:
                        option = int(input("Enter option: "))
                        if option == 9:
                            print("Edit cancelled.")
                            return
                        new_value = input("Enter new value: ")
                        fields = ["first_name", "last_name", "email", "phone_number", "address", "city", "state", "zip"]
                        field = fields[option - 1]
                        ab.edit_contact(first_name=first_name, field=field, new_value=new_value)
                    except (ValueError):
                        print("Invalid input. Edit cancelled.")
            elif len(available_contacts) > 1:
                print("Which one of these contacts you want to edit?: ")
                for i in range(len(available_contacts)):
                    print(f"{i+1}. {available_contacts[i][0]} {available_contacts[i][1]}")
                contact = int(input("\nEnter the contact you want to edit from the above list: "))
                print("\nEnter the detail you want to edit:\n1. First Name\n2. Last Name\n3. Email\n4. Phone Number\n5. Address\n6. City\n7. State\n8. Zip Code\n9. Cancel")
                try:
                    option = int(input("Enter option: "))
                    if option == 9:
                        print("Edit cancelled.")
                        return
                    new_value = input("Enter new value: ")
                    fields = ["first_name", "last_name", "email", "phone_number", "address", "city", "state", "zip"]
                    field = fields[option - 1]
                    ab.edit_contact(first_name=first_name, field=field, new_value=new_value,last_name=available_contacts[contact-1][1])
                except (ValueError):
                        print("Invalid input. Edit cancelled.")
            else:
                print("No contacts available")

                
if __name__ == "__main__":
    AddressBookMain.start() # starting the program using the static method
    while True:
        AddressBookMain.menu()  # displaying the menu options and taking user input