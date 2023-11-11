class People:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def print_info(self):
        print(f"Firstname: {self.firstname}")
        print(f"Lastname: {self.lastname}")
        print(f"Age: {self.age}")