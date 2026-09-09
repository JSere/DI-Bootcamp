#Exercise 1: Favorite Numbers
#Key Python Topics:
#Sets
#Adding/removing items in a set
#Set concatenation (using union)

#Instructions
#Create a set called my_fav_numbers and populate it with your favorite numbers.
#Add two new numbers to the set.
#Remove the last number you added to the set.
#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
#Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {1, 3, 5, 7, 9}
print(my_fav_numbers)

my_fav_numbers.update({11, 13}) #.add()-add 1 number, .update({})-add multiples numbers
print(my_fav_numbers)

my_fav_numbers.remove(13)
print(my_fav_numbers)

friend_fav_numbers = {22, 5, 2, 10, 9}
print(friend_fav_numbers)

union_sets = my_fav_numbers.union(friend_fav_numbers)
print(union_sets)

#Exercise 2: Tuple
#Key Python Topics:
#Tuples (immutability)
#Instructions:
#Given a tuple of integers, try to add more integers to the tuple.
#Hint: Tuples are immutable, meaning they cannot be changed after creation. 
#Think about why you can’t add more integers to a tuple.

tuple_int = (1, 2, 6, 8, 2)
print(tuple_int)

#tuples can not be modified, but we can use this form
new_tuple = tuple_int + (5, 9) 
print(new_tuple)

#Exercise 3: List Manipulation

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
basket.append("Kiwi") # add to the end of the list
basket.insert(0, "Apples") # Add at the beginning
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)

#Exercise 4: Floats

list_nums = []  #create a empty list

for x in range(3, 11):
    if x % 2 == 0:
       list_nums.append(x // 2)
    else:
      list_nums.append(x / 2)        

print(list_nums)          

#Exercise 5: for loop

for x in range(1, 21):
   print(x)

for x in range(1, 21):
   if x % 2 == 0:
      print(x)     

#Exercise 6: While Loop
while True:
   user_name = input("Please enter your name: ").strip()
   if len(user_name) >= 3 and user_name.isalpha():
      #valid name
      break
   else: 
      print("Please enter a real name with at least 3 letters")

print(f"Hello, {user_name}!")

#Exercise 7: Favorite Fruits

fruits = input("Enter fruits separate by commas: ").lower().split(",")
print(fruits)

fruits = [f.strip() for f in fruits]  
print(f"list of fruits: {fruits}")      

fav_fruit = input("name any fruit: ").strip().lower()        
if fav_fruit in fruits:
   print(f"You chose one of your favorite fruits! Enjoy!")
else: 
   print("You chose a new fruit. I hope you enjoy it!") 

 #Exercise 8: Pizza Toppings

pizza_toppings = []

topping = ""

total_cost = 10.0

while topping != "quit":
    topping = input("Enter a topping: ")

    if topping != "quit":
       print(f"Adding {topping} to your pizza. ")
       pizza_toppings.append(topping)
    
       total_cost += 2.50

print(f"Pizza order complete! {pizza_toppings} and the price is: {total_cost}")

#Exercise 9: Cinemax Tickets
family_ages = []
total_cost = 0

while True:
      user_input = input("Enter family member age (or 'quit' to finish): ")

      if user_input.lower() == 'quit':
         break

      age = int(user_input)
      family_ages.append(age)

      if age < 3:
        print("ticket free")
      
      elif age <= 12:
          print("ticket 10")
          total_cost += 10
      else:
          print("ticket 15")    
          total_cost += 15

print(f"total family members: {len(family_ages)}")
print(f"family members ages: {family_ages}")
print(f"total price to pay: ${total_cost}")      


