import random

random_line = random.choice(open("words.txt").read().split('\n'))
print(random_line)
