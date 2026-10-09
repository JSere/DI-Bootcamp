#Challenge 1: Sorting
user_input = input("Enter comma-separated words: ")
word_list = user_input.split(",")
word_list.sort()
sorted_string = ",".join(word_list)
print(sorted_string)


#Challenge 2: Longest Word
def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))