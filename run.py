import random

def get_random_word():
    """
    Picks a random word from words.txt to be used as the word the player has to guess. 
    """
    random_word = random.choice(open("words.txt").read().split('\n'))
    return random_word.upper()


def play_game(word):
    """
    play the game
    """
    word_template = "_" * len(word)
    game_over = False
    guesses = []
    lives = 10
    print("Lets play Hangman!")
    print(f"Lives: {lives}")
    print(f"The word to guess: {word_template}")
    
    while not game_over:
        player_try = input("Guess a letter:\n").upper()
        try:
            if len(player_try) > 1:
                raise ValueError(
                f"You can only guess 1 letter at a time, you guessed {len(player_try)} characters"
            )
            elif not player_try.isalpha():
                raise ValueError(
                f"You can only guess letters, you guessed {(player_try)} which is not a letter"
            )
        except ValueError as e:
            print(f"{e}, please try again.\n")

        
def main():
    """
    Runs the game 
    """
    hangman_word = get_random_word()
    print("Welcome to Hangman!")
    print(hangman_word)
    play_game(hangman_word)

main()
