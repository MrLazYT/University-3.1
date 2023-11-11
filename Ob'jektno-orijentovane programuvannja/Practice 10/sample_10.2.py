class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value

    @age.deleter
    def age(self):
        print(f"Deleting age for {self._name}")
        del self._age

# Використання геттерів, сеттерів і делітерів
person = Person("John", 30)
print(f"Name: {person.name}")
print(f"Age: {person.age}")

person.name = "Jane"
person.age = 25
print(f"Updated Name: {person.name}")
print(f"Updated Age: {person.age}")

del person.age  # Виклик делітера