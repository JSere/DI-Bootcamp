#Exercise 3 : Outputs
#Instructions
#Predict the output of the following code snippets:
#=====================================================

#3 <= 3 < 9    true, using python terminal in visual basic code
#3 == 3 == 3  true
#bool(0) false
#bool(5 == "5") true if something inside bool() will show true, if nothing  or empty inside bool() will be false 
#bool(4 == 4) == bool("4" == "4")# true
#bool(bool(None)) false

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# a will be 5 and b will be 10

#Exercise 4 : How many characters in a sentence ?
#Instructions
#Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
#==========================================================================================

my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(len(my_text))

#Exercise 5: Longest word without a specific character
#Instructions
#Keep asking the user to input the longest sentence they can without the character “A”.
#Each time a user successfully sets a new longest sentence, print a congratulations message.
#==============================================================================================

#ask the user to enter the first sentence
l_sent = input("Welcome! write a sentence without letter 'A': ")

print(f"Your sentence is: {l_sent}")
print(f"Length characters is: {len(l_sent)} ")

while True: # use a bucle infinite, will broke with 'break'
     new_sent = input("Write a longer sentence (or 'exit to stop the game): ")

     if new_sent.lower() == "exit":
          break # end of the bucle 
     
     if "a" in new_sent.lower():
          print("The letter 'A' is not allowed! Try again.")
          continue # go back to begin the bucle

     if len(new_sent) > len(l_sent):
        l_sent = new_sent #actualize the record
        print(f"Congratulations! You have a new record of {len(new_sent)} characters!")  

     elif len(new_sent) == len(l_sent):
         print("Nice try! Same length as the record, but not longer.")   
     else:
         print("The new sentence is shorter than the record.") 