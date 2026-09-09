#Exercise 1: Formula

import math

c = 50
h = 30

while True:
    u_data = input("enter a number or numbers separate by commas to calculate the formula (write 'quit!' to exit): ")
    
    if u_data == 'quit!':
       break 
    
    numbers = u_data.split(",")

    results = []

    for n in numbers:

        d = int(n)
        q = math.sqrt( (2 * c * d) / h)
        results.append(round(q))
    print(f"Result:, {results}")

#Exercise 2 : List of integers

numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 

#print(numbers)
numbers.sort(reverse=True)
sum_numbers = sum(numbers)

print(f"Original list {numbers},\n list in descending order {numbers},\n sum of values {sum_numbers}")

first_number = numbers[0]
last_number = numbers[-1]

first_and_last = [first_number, last_number]

print(f"first and last number: {first_and_last}")

avobe_50 = [n for n in numbers if n > 50] #list comprehension

print(f" numbers > 50: {avobe_50} ") 

smaller_10 = [n for n in numbers if n < 10] #list comprehension

print(f" numbers < 10: {smaller_10} ") 

squared_num = [n**2 for n in numbers] 
print(f"squares numbers: {squared_num}")

#7 numbers without duplicated
unique_num = list(set(numbers)) #set not repeat numbers

unique_count = len(unique_num)

print(f"numbers without duplicates: {unique_num}")
print(f"count of unique numbers: {unique_count}")

average_num = sum(numbers) / len(numbers)
print(f"average: {average_num}")

max_num = max(numbers)
min_num = min(numbers)

print(f"min number is: {min_num}, max number is: {max_num}")

#Exercise 3: Working on a paragraph

paragraph = "Python is an amazing programming language. " \
            "It is versatile, powerful, and easy to learn. " \
            "Many developers use Python for web development, " \
            "data science, and artificial intelligence."

count_characters = len(paragraph)

count_sentences = paragraph.count(".")

total_words = paragraph.split()

count_total_words = len(total_words)

lower_clean_words = [w.lower().strip(".,") for w in total_words]

unique_words = set(lower_clean_words)

count_unique_words = len(unique_words)

print(f"The paragraph will be analyzed:\n" 
      f"count characters: {count_characters}\n" 
      f"count sentences: {count_sentences}\n"
      f"count words: {count_total_words}\n"
      f"count unique words: {count_unique_words}")


#Exercise 4 : Frequency Of The Words

def count_word_frequency(text_input):
    words = text_input.split()
    frequency = {} 

    for w in words:
       if w in frequency:
          frequency[w] = frequency[w] + 1
       else:
          frequency[w] = 1 

    for w in sorted(frequency.keys()):  
        print(f"{w}:{frequency[w]}")

my_text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
count_word_frequency(my_text)