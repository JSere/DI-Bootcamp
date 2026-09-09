# Exercise 1 : Hello World-I love Python
# Instructions write 4 times each sentence, Print the output in one line of code:
#=============================================================================

print("Hello World \nHello World \nHello World \nHello World \nI love Python\nI love Python\nI love Python\nI love Python\n")
#use blackslash and n to get a new line

#Exercise 2 : What is the Season ?
#Instructions
#Ask the user to input a month (1 to 12).
#Display the season of the month received :
#Spring runs from March (3) to May (5)
#Summer runs from June (6) to August (8)
#Autumn runs from September (9) to November (11)
#Winter runs from December (12) to February (2)
#=================================================

month_numb = int(input("This program will tell you the season of the year \nEnter your month number(1 to 12) "))
print(f"your choose month number is: {month_numb}")

if   month_numb == 3 or month_numb == 4 or month_numb == 5:
     print("Spring")

elif month_numb == 6 or month_numb == 7 or month_numb == 8:
     print("Summer")     

elif month_numb == 9 or month_numb == 10 or month_numb == 11:
     print("Autumn")   

elif month_numb == 12 or month_numb == 1 or month_numb == 2:
     print("Winter")

else:
    print("Please use a number between 1 - 12") 