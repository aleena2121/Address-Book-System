import re

def validate_contact(func):  
    """
    Decorator to validate contact details using regex
    """
    def wrapper(*args,**kwargs):
        if kwargs:
            keys = kwargs.copy()
            for key,value in keys.items():
                if 'first_name' == key and  not re.match(r"^[A-Za-z]{2,}$", value):
                    raise ValueError("\nFirst name must contain only letters and be at least 2 characters long.")

                elif 'last_name' == key and not re.match(r"^[A-Za-z]{2,}$", value):
                    raise ValueError("\nLast name must contain only letters and be at least 2 characters long.")

                elif 'email' == key and not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", value):
                    raise ValueError("\nInvalid email format.")

                elif 'phone_number' == key and not re.match(r"(\+?[\d\s]{1,6})?\d{10}$", value):
                    raise ValueError("\nPhone number must be 10 digits long and can have a country code.")
                
                elif 'zip' == key and not re.match(r"^\d{6}$", value):
                    raise ValueError("\nZip code can be only 6 digits long")
        return func(*args,**kwargs)
    return wrapper