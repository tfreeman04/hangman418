class Hangman:
    
    def __init__(self,word_list,num_lives = 5):
        import random
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ["_"]*len(self.word)
        self.num_letters = len(set(self.word.split()))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess!{guess} is in the word")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        while True:
            guess = input("Please enter a letter: ")
            if not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character. ")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            elif len(guess) == 1 and guess not in self.list_of_guesses:
                self.check_guess(guess)
                break
        self.list_of_guesses.append(guess)
        sorted(self.list_of_guesses)

word_list = ["apple","orange","peach","pear","plum"]
hangman_1 = Hangman(word_list)
hangman_1.ask_for_input()




        