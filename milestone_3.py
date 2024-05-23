import random
word_list = ["apple","orange","peach","pear","plum"]

def choice (word_list):
    return random.choice(word_list)
word = choice(word_list)
print(word)
while True:
    guess = input("Please enter a letter: ")
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character. ")

if guess in word:
    print(f"Good guess!{guess} is in the word")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")