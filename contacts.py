class Contact:
    def __init__(self,**kwargs):
        for arg,value in kwargs.items():
            setattr(self, arg, value)  # unpacking all attributes

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} - {self.phone_number}, {self.address}, {self.city}, {self.state} - {self.zip}, {self.email}"
        )

    def to_dict(self):
        return self.__dict__


