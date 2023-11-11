class Vehicle:
    pass

class Car(Vehicle):
    pass

car_instance = Car()

# Перевірка, чи є car_instance екземпляром класу Car
if isinstance(car_instance, Car):
    print("car_instance is an instance of Car class")

# Перевірка, чи є car_instance екземпляром класу Vehicle (або його підкласів)
if isinstance(car_instance, Vehicle):
    print("car_instance is an instance of Vehicle class or its subclasses")