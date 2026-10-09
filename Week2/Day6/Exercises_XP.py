#Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
    
cat1 = Cat("Max", 5)        
cat2 = Cat("Lili", 8)
cat3 = Cat("Rocky", 3)

def get_age(c):
    return c.age

oldest = max(cat1, cat2, cat3, key=get_age)

print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")
    
#Exercise 2: Dogs

class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print(f"{self.name} goes woof")

    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high!")    

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Roxy", 35)

print(f"Davids dog: {davids_dog.name}, height: {davids_dog.height}cm") 
davids_dog.bark()
davids_dog.jump()

print(f"\nSarahs dog: {sarahs_dog.name}, height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"\n{davids_dog.name} is bigger than {sarahs_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"\n{sarahs_dog.name} is bigger than {davids_dog.name}.")
else:
    print("\nBoth dogs are the same size!")

#Exercise 3 : Who’s the song producer?

class Song:
    def __init__(self, song_lyrics):
        self.lyrics = song_lyrics

    def sing_me_a_song(self):
        for l in self.lyrics:
            print(l)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#Exercise 4 : Afternoon at the Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print(f"Animals in {self.zoo_name}:")
        for animal in self.animals:
            print(f"- {animal}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        groups = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in groups:
                groups[first_letter] = [animal]
            else:
                groups[first_letter].append(animal)
        return groups

    def get_groups(self):
        grouped_animals = self.sort_animals()
        for letter, animal_list in grouped_animals.items():
            print(f"{letter}: {animal_list}")


brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Cat", "Cougar", "Zebra")
brooklyn_safari.get_animals()

brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()

brooklyn_safari.get_groups()


