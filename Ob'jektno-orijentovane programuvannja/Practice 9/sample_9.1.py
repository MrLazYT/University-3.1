class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Використання поліморфізму
dog = Dog()
cat = Cat()

print(dog.make_sound())
print(cat.make_sound())