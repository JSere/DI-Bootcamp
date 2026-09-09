#Challenge 1: Multiples of a Number

base_number = int(input("enter the base number: "))

list_length = int(input("enter the length of the list: "))

multiples_list = []

for i in range(1, list_length + 1):

    result = base_number * i
    multiples_list.append(result) 

print(multiples_list)

#Challenge 2: Remove Consecutive Duplicate Letters

user_string = input("enter a string: ")

unique_string = []

for letter in user_string:

    if len(unique_string) == 0:
        unique_string.append(letter) 
    
    elif letter != unique_string[-1]:
        unique_string.append(letter)

clean_text = "".join(unique_string)

print(f"letra actual:, {clean_text}")

