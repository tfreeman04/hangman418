import random

word_list = ["apple","orange","peach","pear","plum"]


def choice (word_list):
    return random.choice(word_list)

word = choice(word_list)
print(word)
