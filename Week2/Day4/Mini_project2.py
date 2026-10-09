import random

def get_hangman_art(failures):
    stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
               |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
         ========="""
    ]
    return stages[failures]

def play_hangman():
    words = ["python", "computer", "program", "code", "game", "keyboard"]
    secret_word = random.choice(words)
    hidden_word = ["*"] * len(secret_word)
    guessed_letters = []
    failures = 0
    max_failures = 6

    print("--- WELCOME TO HANGMAN GAME ---")

    while failures < max_failures and "*" in hidden_word:
        print(get_hangman_art(failures))
        print("\nWord: " + " ".join(hidden_word))
        print("Guessed letters: " + ", ".join(guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good job! The letter '{guess}' is in the word.\n")
            for index in range(len(secret_word)):
                if secret_word[index] == guess:
                    hidden_word[index] = guess
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.\n")
            failures += 1

    print(get_hangman_art(failures))
    if "*" not in hidden_word:
        print("Congratulations! You guessed the word:", secret_word)
    else:
        print("Game Over! You ran out of attempts.")
        print("The secret word was:", secret_word)

play_hangman()