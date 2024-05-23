import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.num_letters = len(set(self.word))

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
            print(" ".join(self.word_guessed))
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Please enter a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(f"List of guesses: {self.list_of_guesses}")
                break

def play_game(word_list):
    game = Hangman(word_list)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif "_" not in game.word_guessed:
            print("Congratulations! You won the game.")
            break
        else:
            game.ask_for_input()

word_list = ["apple", "orange", "peach", "pear", "plum"]
play_game(word_list)