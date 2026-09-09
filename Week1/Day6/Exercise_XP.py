# Exercise 1: Converting Lists into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

concat = zip(keys, values)

my_dict = dict(concat)

print(my_dict)

#Exercise 2: Cinemax #2
#bonus
family = {}

print("enter family members(type 'quit' as the name to finish)")

while True:
   name = input("enter a name: ")
   if name.lower() == 'quit':
      break
   
   age = int(input(f"enter age for {name}: "))

   family[name] = age
   print("-" * 30)


total_cost = 0

for name, age in family.items():
    if age < 3:
       ticket_price = 0
    elif 3 <= age <= 12:
       ticket_price = 10
    else:
       ticket_price = 15

    print(f"{name}:  ${ticket_price} (age: {age})")

    total_cost += ticket_price

print(f"\nthe total family cost is: ${total_cost}") 

#Exercise 3: Zara
brand = {

"name": "Zara",
"creation_date": 1975,
"creator_name":"Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home"],
"international_competitors": ["Gap", "H&M", "Benetton"],
"number_stores": 7000,
"major_color": {
    "France": "blue", 
    "Spain": "red", 
    "US": ["pink", "green"]
   }
}

brand["number_stores"] = 2

print(f"Zara's client could be: {brand["type_of_clothes"]}")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

brand.pop("creation_date")

print(f"The last competitor is: {brand["international_competitors"][-1]}")
print(f"The major colors in us are: {brand['major_color']['US']}")
print(f"the intems in Zara's collections are: {list(brand.keys())}")
print(f"numbers of keys in Zara brand are: {len(brand)}")
print(brand)

#Exercise 4: Disney Characters

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

users = sorted(users)

character_to_index = {}

for i in range(len(users)):
    
    character = users[i]

    character_to_index[character] = i

print(character_to_index)

index_to_character = {}

for i in range(len(users)):
    
    character = users[i]

    index_to_character[i] = character

print(index_to_character)    








