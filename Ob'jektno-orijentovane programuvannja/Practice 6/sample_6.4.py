class People:
    count = 0 # Змінна класу.

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        People.count += 1
    
    def print_info(self):
        print(f"Firstname: {self.firstname}")
        print(f"Lastname: {self.lastname}")
        print(f"Age: {self.age}")

mike = People("Mike", "Stark", 20)
bob = People("Bob", "Stone", 19)
joel = People("Joel", "Miller", 25)

mike.print_info()
People.print_info(bob)
People.print_info(joel)

print(f"Object count: {People.count}")