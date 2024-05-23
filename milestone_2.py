import random

word_list = ["apple","orange","peach","pear","plum"]


def choice (word_list):
    return random.choice(word_list)

word = choice(word_list)
# testing choice method 
#print(word)
guess = input("Please enter a single letter: ")
if len(guess) == 1 and type(guess) == str:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

