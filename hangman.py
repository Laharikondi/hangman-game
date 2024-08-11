import random

def get_random_word(word_list):
    return random.choice(word_list).upper()

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    word_list = ['PYTHON', 'DEVELOPER', 'PROGRAM', 'HANGMAN', 'COMPUTER']
    word = get_random_word(word_list)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6
    
    print("Welcome to Hangman!")

    while wrong_guesses < max_wrong_guesses:
        print("\nWord: " + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").upper()

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word. You have {max_wrong_guesses - wrong_guesses} guesses left.")
        
        if set(word) <= guessed_letters:
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    play_hangman()
