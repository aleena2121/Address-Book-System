from address_book import AddressBook
from address_book_system import AddressBookSystem
from Schema import schema

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
        print("\nMenu:\n1. Add new Contact\n2. Display Contacts\n3. Edit Contact\n4. Delete Contact\n5. Exit")  # menu options for user
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
            elif option == 5:  # exits the program
                print("\nGoodbye!")
                exit()
            else:
                print("Invalid option")
        except ValueError:
            print("Please enter a valid number")

    @staticmethod
    def add_contact():
        """
        Fucntion to get input from user to add contact and to add it in address book
        """
        details = schema.ContactSchema(  # using the schema defined for contact class
            first_name=input("First name: "),
            last_name=input("Last name: "),
            email=input("Email: "),
            phone_number=input("Phone number: "),
            address=input("Address: "),
            city=input("City: "),
            state=input("State: "),
            zip=input("Zip Code: ")
        )
        name = input("Please enter Address Book Name: ")  # getting address book name from user
        ab = AddressBookMain.system.get_address_book(name)
        try:
            ab.add_contact(**details.__dict__)  # passing the values as a dictionary
        except ValueError as e:
            print(e)

    @staticmethod
    def display_contacts():
        """
        Fucntion to display all contacts in an address book
        """
        name = input("\nEnter Address Book Name to display contacts: ")
        ab = AddressBookMain.system.get_address_book(name)
        if ab.contacts:
            print(f"\nContacts in {ab.address_book_name}: ")
            for contact in ab.contacts:
                print(contact)
        else:
            print("No contacts found.")

    @staticmethod
    def edit_contact():
        """
        Fucntion to get input from user to edit contact and edit it correspondingly in address book
        """
        name = input("Please enter Address Book Name in which you want to edit the contact: ")
        ab = AddressBookMain.system.get_address_book(name)
        if ab:
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
                    
                fields = ["first_name", "last_name", "email", "phone_number", 
                        "address", "city", "state", "zip"]
                field = fields[option - 1]
                new_value = input("Enter new value: ")
                
                try:
                    ab.edit_contact(
                        first_name=first_name,
                        last_name=last_name,
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
        name = input("\nPlease enter Address Book Name in which you want to delete the contact: ")
        ab = AddressBookMain.system.get_address_book(name)
        if ab:
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

            else:
                print("No contacts available")


                
if __name__ == "__main__":
    AddressBookMain.start() # starting the program using the static method
    while True:
        AddressBookMain.menu()  # displaying the menu options and taking user input