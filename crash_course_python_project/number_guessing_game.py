# Exam 1: Number Guessing Game 🎲 (Mandatory)
# Build a fun Number Guessing Game in Python! 🐍 The program picks a random number between 1-100,
# and you have 7 attempts to guess it. Get hints if you’re too high 📈 or too low 📉!,
# Perfect for practicing loops 🔄, conditionals ❓, and user input ⌨️.
#=============================================================================================


import random                     

# import random module to generate random numbers 

def number_guessing_game():
    print("Welcome to the game")
# define funtion 'def number_guessing_game' and welcome to the user     

    random_number =random.randint(1, 100)
    max_attempts = 7
# defining numbers parametres for the program 

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess < random_number:
          print("Too low!")
        elif guess > random_number:
          print("Too high")    
        else:
          print(f"Correct! You guessed the number in {attempt} attempts!")
          break 
    else:
        print(f"Game over! The number was {random_number}")        
#create a loop with random numbers
#ask an user attempt with a number guessing 
#use a conditional and will show some hints to the user   

number_guessing_game() 
#run the program   