class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin
        self.__secret_identity = f"{name} from {origin}"  

    def show_identity(self):
        print(f"{self.name}'s secret identity is hidden.")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Derived class
class Flyer(Superhero):
    def __init__(self, name, origin):
        super().__init__(name, power="Flight", origin=origin)

    def use_power(self):
        print(f"{self.name} takes off into the skies!")

class Speedster(Superhero):
    def __init__(self, name, origin):
        super().__init__(name, power="Super Speed", origin=origin)

    def use_power(self):
        print(f"{self.name} zooms past in a blur!")

# Create superhero objects
hero1 = Flyer("SkyBolt", "Cloud City")
hero2 = Speedster("FlashStrike", "Quantum Realm")

hero1.use_power()
hero2.use_power()
hero1.show_identity()
# Base class
class Animal:
    def move(self):
        print("This animal moves in its own way.")

# Derived classes with polymorphic behavior
class Dog(Animal):
    def move(self):
        print("Dog runs energetically 🐶")

class Fish(Animal):
    def move(self):
        print("Fish swims gracefully 🐟")

class Bird(Animal):
    def move(self):
        print("Bird flies elegantly 🕊️")

# Using polymorphism
animals = [Dog(), Fish(), Bird()]
for animal in animals:
    animal.move()
