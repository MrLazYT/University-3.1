class Vehicle:
    pass

class Car(Vehicle):
    pass

class Bus(Vehicle):
    pass

# Перевірка, чи є клас Car підкласом класу Vehicle
if issubclass(Car, Vehicle):
    print("Car is a subclass of Vehicle")

# Перевірка, чи є клас Bus підкласом класу Vehicle
if issubclass(Bus, Vehicle):
    print("Bus is a subclass of Vehicle")