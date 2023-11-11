class People:
    count = 0

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

        People.count += 1
        
    def print_info(self):
        print(f"Firstname: {self.firstname}")
        print(f"Lastname: {self.lastname}")
        print(f"Age: {self.age}")
    
    @classmethod
    def return_count(cls):
        print("This is a class method!")
        print(f"Total object count: {cls.count}")

person1 = People("Joel", "Miller", 35)
person2 = People("Elly", "Ramsey", 20)

People.return_count()