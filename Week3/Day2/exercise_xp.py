#1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_obj = Bengal("Simba", 3)
chartreux_obj = Chartreux("Cleo", 5)
siamese_obj = Siamese("Maya", 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = Pets(all_cats)
sara_pets.walk()

#2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}!"
        elif self_power < other_power:
            return f"{other_dog.name} won the fight against {self.name}!"
        else:
            return f"It's a tie between {self.name} and {other_dog.name}!"

dog1 = Dog("Rex", 4, 20)
dog2 = Dog("Max", 6, 25)
dog3 = Dog("Rocky", 3, 15)

print(dog1.bark())
print(f"{dog2.name}'s running speed: {dog2.run_speed()}")
print(dog1.fight(dog2))

#3
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [self.name] + list(args)
        names_str = ", ".join(dog_names)
        print(f"{names_str} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            chosen_trick = random.choice(tricks)
            print(f"{self.name} {chosen_trick}")
        else:
            print(f"{self.name} is not trained yet!")

my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max", "Charlie")
my_dog.do_a_trick()

#4
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents accept that you will go out with your friends")
                else:
                    print(f"Sorry, {first_name}, you are not allowed to go out with your friends.")
                return
        print(f"Family member named {first_name} not found.")

    def family_presentation(self):
        print(f"Family Last Name: {self.last_name}")
        print("Family Members:")
        for member in self.members:
            print(f"- {member.first_name}, {member.age} years old")

my_family = Family("Smith")

my_family.born("John", 45)
my_family.born("Jane", 42)
my_family.born("Alice", 16)
my_family.born("Bob", 20)

my_family.family_presentation()

print("\n--- Checking Majorities ---")
my_family.check_majority("Alice")
my_family.check_majority("Bob")
