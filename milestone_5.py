import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Initialize the game with a word list and a default number of lives
        self.word_list = word_list
        self.word = random.choice(word_list)  # Randomly choose a word from the list
        self.word_guessed = ["_"] * len(self.word)  # Initialize the guessed word with underscores
        self.num_lives = num_lives  # Set the number of lives
        self.list_of_guesses = []  # Initialize an empty list to track guesses
        self.num_letters = len(set(self.word))  # Count of unique letters in the word

    def check_guess(self, guess):
        # Method to check if the guessed letter is in the word
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess  # Reveal the guessed letter in the word
            self.num_letters -= 1  # Decrease the count of unique letters left to guess
            print(" ".join(self.word_guessed))  # Print the current state of the guessed word
        else:
            self.num_lives -= 1  # Decrease the number of lives if the guess is incorrect
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        # Method to ask the player for a letter input
        while True:
            guess = input("Please enter a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                # Check if the input is a single alphabetical character
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                # Check if the letter has already been guessed
                print("You already tried that letter!")
            else:
                # If valid input, check the guess and add it to the list of guesses
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(f"List of guesses: {self.list_of_guesses}")
                break  # Exit the loop after processing the guess

def play_game(word_list):
    # Function to play the game
    game = Hangman(word_list)  # Initialize a new game instance
    while True:
        if game.num_lives == 0:
            # Check if the player has run out of lives
            print("You lost!")
            break
        elif "_" not in game.word_guessed:
            # Check if the player has guessed all the letters
            print("Congratulations! You won the game.")
            break
        else:
            # Continue to ask for input if the game is not over
            game.ask_for_input()

# List of words to be used in the game
word_list = ["apple", "orange", "peach", "pear", "plum"]
play_game(word_list)  # Start the game