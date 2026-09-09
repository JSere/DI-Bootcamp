#Exercise 1: Concatenate list

list = [1, 2, 5]
list2 = [6,9,7]
list.extend(list2)
print(list) # using method extend

#Exercise 2: Range of numbers

#option a:
num = list(range(1500, 25001))

for n in num:

   if n % 5 == 0 and n % 7 == 0:
    print(n)

#option b:
filtered_num = [n for n in range(1500, 25001) if n % 5 == 0 and n % 7 == 0]    
print(filtered_num)  

#Exercise 3: Check the index

#a
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
   
user_input = input("Enter a name to check: ")
   
if user_input in names:
     print(user_input)
else:
     print("No")

#b
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
   
user_input = input("Enter a name to check: ")
   
if user_input in names:
    # Use the .index() method to find the position
    position = names.index(user_input)
    print(position)
else:
    print("No") 

#Exercise 4: Greatest Number

#a
user_num1 = input("Enter first number: ")

user_num2 = input("Enter the second number: ")

user_num3 = input("Enter the thrid number: ")

print(f"your number are {user_num1}, {user_num2} and {user_num3} ")

if user_num1 > user_num2 and user_num1 > user_num3:
   print(f"The greatest number is {user_num1}")

elif user_num2 > user_num1 and user_num2 > user_num3:
   print(f"The greates number is {user_num2}")    

else:
    print(f"The greates number is {user_num3}")

#b
user_num1 = int(input("Enter first number: "))

user_num2 = int(input("Enter the second number: "))

user_num3 = int(input("Enter the thrid number: "))

all_numbers = [user_num1, user_num2, user_num3]

print(f"your numbers are {all_numbers} ")

greatest_num = max(all_numbers)

print(f"The greatest number is {greatest_num}")


#Exercise 5: The Alphabet

alphabet_string = "abcdefghijklmnopqrstuvwxyz"

alphabet_list = list(alphabet_string)

for letter in alphabet_list:

    if letter in "aeiou":
       print(f" {letter} is vowel")
    else:
        print(f" {letter} is consonant") 

#Exercise 6: Words and letters   

words = []

for i in range(7):
    word = input(f"Enter the word {i+1} of 7: ")
    words.append(word)

print("\nYour 7 words are: ")
print(words)

letter = input("Enter a single character to search for: ")

for w in words:
    
    index = w.find(letter)
    
    if index != -1:
        print(f"Found! {letter} in {w} at index {index}")
    else:
        print(f"{letter}! is missing in {w} ")

#Exercise 7: Min, Max, Sum

list_n = []

for l in range(1, 1000001):
    list_n.append(l)

print(list_n)

max_num = max(list_n)
min_num = min(list_n)
sum_num = sum(list_n)

print(f"The minimum number is: {min_num}, the max number is: {max_num} and the sum number is: {sum_num}")

#Exercise 8 : List and Tuple

u_input = input("Enter numbers spaced by commas: ")

list_exe_8 = u_input.split(",")

tuple_exe_8 = tuple(list_exe_8)

print(f"list: {list_exe_8} and tuple: {tuple_exe_8}")

#Exercise 9 : Random number
import random

user_n = int(input("enter a digit between 1 and 9(including):"))
random_n = random.randint(1, 9)

if user_n == random_n:
    print("winner")
else:
    print("better luck next time")    
print(f"user number is: {user_n} and random number is: {random_n}")

#Exercise 9: Random number + bonus
import random

while True:
    user_n = int(input("enter a digit between 1 and 9(or 0 to quit):"))
    
    if user_n == 0:
       print("Exiting the game. Bye :(")
       break
    
    random_n = random.randint(1, 9)

    if user_n == random_n:
       print("winner")
    else:
       print("better luck next time")    
    print(f"user number is: {user_n} and random number is: {random_n}")











