from contacts import Contact
from address_book import AddressBook   
import re

def validate_contact(func):
    def wrapper(*args, **kwargs):
        details = kwargs['details']

        if not re.match(r"^[A-Za-z]{2,}$", details['first_name']):
            raise ValueError("First name must contain only letters and be at least 2 characters long.")
        
        if not re.match(r"^[A-Za-z]{2,}$", details['last_name']):
            raise ValueError("Last name must contain only letters and be at least 2 characters long.")
        
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", details['email']):
            raise ValueError("Invalid email format.")
        
        if not re.match(r"^\+?\d{10,12}$", details['phone_number']):
            raise ValueError("Phone number must be 10 to 12 digits long.")
        
        return func(*args, **kwargs)
    return wrapper


class AddressBookMain:
    @staticmethod
    def start():
        print("Welcome to Address Book Program!!")

    @staticmethod
    def menu():
        option = input("Enter 'new' to add a new contact: ")
        match option:
            case "new":
                details = {}
                print("Enter contact details:")
                details["first_name"] = input("First name: ")
                details["last_name"] = input("Last name: ")
                details["email"] = input("Email: ")
                details["phone_number"] = input("Phone number: ")
                details["address"] = input("Address: ")
                details["city"] = input("City: ")
                details["state"] = input("State: ")
                details["zip"] = input("Zip Code: ")


if __name__ == "__main__":
    AddressBookMain.start()
    AddressBookMain.menu()