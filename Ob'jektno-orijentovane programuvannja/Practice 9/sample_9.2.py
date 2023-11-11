class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

    def __str__(self):
        return f"{self.name} is an Animal"

    def __repr__(self):
        return f"Animal('{self.name}')"

    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.name == other.name
        return False


class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def __str__(self):
        return f"{self.name} is a Dog"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"

    def __str__(self):
        return f"{self.name} is a Cat"


# Використання магічних методів
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(str(dog))  # Вивід: Buddy is a Dog
print(str(cat))  # Вивід: Whiskers is a Cat

print(repr(dog))  # Вивід: Animal('Buddy')
print(repr(cat))  # Вивід: Animal('Whiskers')

another_dog = Dog("Buddy")
print(dog == another_dog)  # Вивід: True

another_cat = Cat("Mittens")
print(cat == another_cat)  # Вивід: False