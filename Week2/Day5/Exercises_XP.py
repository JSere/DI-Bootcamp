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

dog1 = Dog("Rufy", 2) 
dog2 = Dog("Boby", 4)