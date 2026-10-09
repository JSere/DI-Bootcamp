#Exercise 1: What Are You Learning?

def display_message():
    print ("I am learning about functions in Python.")

display_message()    

# Exercise 2: What’s Your Favorite Book?

def favorite_book(title):
    print(f"my favorite book is: {title}")

favorite_book("harry potter")

#Exercise 3: Some Geography

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}")

describe_city('Reykjavik', 'Iceland')
describe_city('Paris')

#Exercise 4: Random

import random

def check_number(user_number):

  random_num = random.randint(1, 100)    
  if random_num == user_number:
     print("Succes!")
  else:
     print(f"Fail! Your number: {user_number}, Random number: {random_num}") 


check_number(20)

#Exercise 5: Let’s Create Some Personalized Shirts!

def make_shirt(size="large", text="I love python"):
    print(f"the shirt size is {size} and the message is {text} ")

make_shirt()
make_shirt("medium")
make_shirt("small", text="I eat")
make_shirt(size="small", text="Hello!")

#Exercise 6: Magicians…

magicians_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

for i in range(len(magicians_names)):
    print(f"{magicians_names[i]} 'The Great' ")

import random

def get_random_temp():
    return random.randint(-10, 40)

def main():
    temp = get_random_temp()
    print(f"the temperature right now is {temp} degress Celsius")

    if temp < 0:
       print("Brrr, that’s freezing! Wear some extra layers today.")  

    elif 0 <= temp <= 16:
         print("Quite chilly! Don’t forget your coat.") 

    elif 17 <= temp <= 23:
        print("Nice weather.")

    elif 24 <= temp <= 32:
         print("A bit warm, stay hydrated.")

    else: 
        print("It’s really hot! Stay cool.") 

main()