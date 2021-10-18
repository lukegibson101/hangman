import random


def get_random_word():
    """
    Picks a random word from words.txt to be used as the word the player has
    to guess.
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
    print(f"The word to guess: " + " ".join(word_template))

    while not game_over and lives > 1:
        player_try = input("Guess a letter:\n").upper()
        try:
            if len(player_try) > 1:
                raise ValueError(
                    f"You can only guess 1 letter at a time, you guessed
                    {len(player_try)} characters"
                )

            elif not player_try.isalpha():
                raise ValueError(
                    f"You can only guess letters, you guessed
                    {(player_try)} which is not a letter"
                )

            elif len(player_try) == 1 and player_try.isalpha():
                if player_try in guesses:
                    raise ValueError(
                        f"You have already guessed {(player_try)}"
                    )

                elif player_try not in word:
                    print(
                        f"{(player_try)} is not in the word. You lose a life"
                    )
                    guesses.append(player_try)
                    lives -= 1

                else:
                    print(
                        f"{player_try} is in the word. Well done!\n"
                    )
                    guesses.append(player_try)
                    word_template_list = list(word_template)
                    indices = [i for i, letter in enumerate(word)
                               if letter == player_try]
                    for index in indices:
                        word_template_list[index] = player_try
                        word_template = "".join(word_template_list)
                    if "_" not in word_template:
                        game_over = True

        except ValueError as e:
            print(f"{e}, please try again.\n")
            continue

        print(f"Lives: {lives}")
        print(f"The word to guess: " + " ".join(word_template))
        print(guesses)

    print("GAME OVER")


def main():
    """
    Runs the game
    """
    hangman_word = get_random_word()
    print("Welcome to Hangman!")
    print(hangman_word)
    play_game(hangman_word)


main()
