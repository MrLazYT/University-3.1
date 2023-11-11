class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")


class Bus(Vehicle):
    def __init__(self, make, model, year, num_seats):
        super().__init__(make, model, year)
        self.num_seats = num_seats

    def display_info(self):
        super().display_info()
        print(f"Number of Seats: {self.num_seats}")


# Приклад використання класів
car = Car("Toyota", "Camry", 2022, 4)
bus = Bus("Mercedes", "Sprinter", 2020, 20)

# Виведення інформації про транспортні засоби
print("Car Information:")
car.display_info()

print("\nBus Information:")
bus.display_info()