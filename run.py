import random


# def get_random_word():
random_line = random.choice(open("words.txt").read().split('\n'))
print(random_line.upper())
