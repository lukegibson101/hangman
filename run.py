import random

def get_random_word():
    """
    Picks a random word from words.txt to be used as the word the player has to guess. 
    """
    random_word = random.choice(open("words.txt").read().split('\n'))
    return random_word.upper()


def main():
    """
    Runs the game 
    """
    hangman_word = get_random_word()
    print("Lets play hangman!")


main()
