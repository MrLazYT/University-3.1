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
    
    @classmethod
    def from_birth_year(cls, firstname, lastname, birth_year):
        age = 2023 - birth_year

        return cls(firstname, lastname, age)
    
    @staticmethod
    def is_adult(age):
        return age >= 18

person1 = People.from_birth_year("Elly", "Ramsey", 2003)
person1.print_info()

print(f"Is {person1.firstname} {person1.lastname} adult?")
print(People.is_adult(person1.age))