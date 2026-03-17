# Exercise 1: Hello World
#===================================

# option 1 using print and \n

print("Hello world\nHello world\nHello world\nHello world")

#option 2 using loop

for i in range(4):
    print("Hello world")

# Exercise 2: Some Math
# Instructions
# Write code that calculates the result of:
# (99^3)*8 (meaning 99 to the power of 3, times 8).
#=================================================

result = (99**3)*8
print(result)

# Exercise 3: What is the output?
# Instructions
# Predict the output of the following code snippets:
# Coment what is your guess, then run the code and compare
#=========================================================

is_less_example = 15 < 8 # false
print(is_less_example)

is_less1 = 5 < 3  # false
print(is_less1)

is_equal1 = 3 == 3  # true
print(is_equal1)

is_equal2 = 3 == "3" # false
print(is_equal2)

'''is_less2 = "3" > 3 # error, compare need to use numbers, int, float... 
print(is_less2)'''

is_less3 = "Hello" == "hello" # false
print(is_less3)

# Exercise 4: Your computer brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following:
# "I have a <computer_brand> computer."
#==============================================================

computer_brand = "asus"
print(f"I have a {computer_brand} computer")

#Exercise 5: Your information
#=======================================

name = "juan"  
age = 25
shoe_size = 44
info = f"my name is {name}, I am {age} years old, and my shoes size is {shoe_size}" #use f string to conect all the variables in one sentece

print(info)

#Exercise 6: A & B
#======================

a = 5
b = 3

if a > b:
   print("Hello world")

#Exercise 7: Odd or Even
#Write code that asks the user for a number and determines whether this number is odd or even.
#==================================================================================

print("This program will help you to check if the number you enter is an Odd or Even")
number = int(input("Enter a number: "))
print(f"the number is: {number}")             

#Use conditional and evaluate if number, when is divide by 2, has no remainder
#if is true is Even, otherwise is Odd

if number % 2 == 0:                      
   print(f"The number {number} is Even")  
else:
   print(f"The number {number} is Odd")   

#Exercise 8: What’s your name?
#=======================================

name1 = "juan"

user_name = input("What is your name: " )
print(f"Hello {user_name} ")

if name1 == user_name:
   print("what a coincidence we have the same name :)")
if name1 != user_name:
   print("we have differents names by we share the same planet")   

# Exercise 9: Tall enough to ride a roller coaster
#Instructions
#Write code that will ask the user for their height in centimeters.
#If they are over 145 cm, print a message that states they are tall enough to ride.
#If they are not tall enough, print a message that says they need to grow some more to ride.
# =================================================

height = int(input("Welcome to Roller Coaster game! \nEnter your height in cm: "))
print(f"your height is: {height}")
#ask the user the high

if height >= 145:
   print("you are tall enough to ride")
else:
   print("you need to grow some more to ride")  
#use a conditional to check the value


