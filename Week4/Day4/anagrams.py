import os
from anagram_checker import AnagramChecker

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "sowpods.txt")
    
    checker = AnagramChecker(file_path)
    
    while True:
        print("\n--- Menu ---")
        print("1. Input a word")
        print("2. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            user_input = input("Enter a word: ").strip()
            
            words = user_input.split()
            if len(words) != 1:
                print("Error: Only a single word is allowed.")
                continue
                
            word = words[0]
            
            if not word.isalpha():
                print("Error: Only alphabetical characters are allowed (no numbers or special characters).")
                continue
                
            word_upper = word.upper()
            
            if not checker.is_valid_word(word_upper):
                print(f"'{word_upper}' is not a valid English word.")
                continue
                
            anagrams_list = checker.get_anagrams(word_upper)
            
            print(f'\nYOUR WORD : "{word_upper}"')
            print("this is a valid English word.")
            if anagrams_list:
                print(f"Anagrams for your word: {', '.join(anagrams_list)}.")
            else:
                print("No anagrams found for your word.")
                
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()