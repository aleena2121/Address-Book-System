class Contact:
    def __init__(self,first_name,last_name,phone_number,address,city,state,zip,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.email = email

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} - {self.phone_number}, {self.address}, {self.city}, {self.state} - {self.zip}, {self.email}"
        )

