import random


class text_colors:
    YELLOW = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'


def initialise_game():
    """
    Option to begin game or select difficulty
    """
    print ("Press " + text_colors.YELLOW + "1" + text_colors.WHITE +
           " to play game")
    print ("Press " + text_colors.YELLOW + "2" + text_colors.WHITE +
           " to set difficulty")
    print("Press " + text_colors.YELLOW + "3" + text_colors.WHITE +
          " to view rules")
    options = False
    while not options:
        settings = input("\n")
        if settings == "1":
            options = True
            difficulty = "default"
            return difficulty

        elif settings == "2":
            options = True

        elif settings == "3":
            options = True
            game_rules()

        else:
            print(text_colors.RED + "Please select 1, 2 or 3 to make your"
                  " choice" + text_colors.WHITE)


def select_difficulty():
    """
    Let player set difficulty
    """
    print("\n")
    print("Select Difficulty\n")
    print(
        "Press " + text_colors.YELLOW + "E" + text_colors.WHITE + " for Easy"
        )
    print(
        "Press " + text_colors.YELLOW + "N" + text_colors.WHITE + " for Normal"
        )
    print(
        "Press " + text_colors.YELLOW + "H" + text_colors.WHITE + " for Hard"
        )
    difficulty = False
    while not difficulty:
        options = input("\n").upper()
        if options == "E":
            difficulty = True
            num_lives = 10
            return num_lives
        elif options == "N":
            difficulty = True
            num_lives = 7
            return num_lives
        elif options == "H":
            difficulty = True
            num_lives = 5
            return num_lives
        else:
            print(text_colors.RED + "\nPlease select E, N or H to make your"
                  " choice" + text_colors.WHITE)


def get_random_word():
    """
    Picks a random word from words.txt to be used as the word the player has
    to guess.
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    return random_word.upper()


def play_game(word, num_lives):
    """
    Play the game.
    Sets initial lives and template for player to play on.
    When game over calls game over graphics and restart game functions
    which gives player option to restart or go to main menu.
    """
    word_template = "_" * len(word)
    game_over = False
    guesses = []
    lives = num_lives
    print("\n")
    print(text_colors.BOLD + "Lets play Hangman!\n" + text_colors.WHITE)
    print(f"Lives: {lives}\n")
    print(f"The word to guess: " + " ".join(word_template) + "\n")

    while not game_over and lives > 0:
        player_try = input(text_colors.YELLOW + "Guess a letter:\n" +
                           text_colors.WHITE).upper()
        try:
            if len(player_try) > 1:
                raise ValueError(
                    f"You can only guess 1 letter at a time, you guessed"
                    f" {len(player_try)} characters"
                )

            elif not player_try.isalpha():
                raise ValueError(
                    f"You can only guess letters, you guessed {(player_try)}"
                    f" which is not a letter"
                )

            elif len(player_try) == 1 and player_try.isalpha():
                if player_try in guesses:
                    raise ValueError(
                        f"You have already guessed {(player_try)}"
                    )

                elif player_try not in word:

                    message = f"{text_colors.RED}{(player_try)} is not in the"\
                              f" word. You lose a life.{text_colors.WHITE}"

                    guesses.append(player_try)
                    lives -= 1

                else:

                    message = f"{text_colors.GREEN}{player_try} is in the"\
                              f" word. Well done!{text_colors.WHITE}"

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
            print(f"{text_colors.RED}\n{e}.\nPlease try again.\n"
                  f"{text_colors.WHITE}")
            continue

        print(hangman_lives(lives))

        if lives > 0:
            print(message)
            print(f"Lives: {lives}\n")
            print(f"The word to guess: " + " ".join(word_template) + "\n")
            print("Letters guessed: " + ", ".join(sorted(guesses)))

    if game_over:
        print(f"\n{text_colors.GREEN}Congratulations. {word} was the correct"
              f" word!{text_colors.WHITE}")
        player_wins()

    else:
        print(f"{text_colors.RED}The correct word was {word}"
              f"{text_colors.WHITE}")
        hangman_wins()

    restart_game(num_lives)


def restart_game(num_lives):
    """
    Gives player option to restart, otherwise returns to title screen
    """
    game_restart = False

    while not game_restart:
        restart = input(f"Would you like to play again? {text_colors.YELLOW}"
                        f"Y/N{text_colors.WHITE}\n").upper()
        try:
            if restart == "Y":
                game_restart = True
                hangman_word = get_random_word()

                play_game(hangman_word, num_lives)

            elif restart == "N":
                game_restart = True
                print("\n")
                main()

            else:
                raise ValueError(
                    f"You must type in Y or N. You typed {(restart)}"
                )

        except ValueError as e:
            print(f"{text_colors.RED}{e}.\nPlease try again.\n"
                  f"{text_colors.WHITE}")


def player_wins():
    """
    Display You Win! graphic
    """
    print(
        text_colors.GREEN + """
        __   __
        \\ \\ / /__  _   _
         \\ V / _ \\| | | |
          | | (_) | |_| |
          |_|\\___/_\\__,_| _
        __      _(_)_ __ | |
        \\ \\ /\\ / / | '_ \\| |
         \\ V  V /| | | | |_|
          \\_/\\_/ |_|_| |_(_)
        """ + text_colors.WHITE
        )


def hangman_wins():
    """
    Display Game Over! graphic
    """
    print(
        text_colors.RED + """
          ____
         / ___| __ _ _ __ ___   ___
        | |  _ / _` | '_ ` _ \\ / _ \\
        | |_| | (_| | | | | | |  __/
         \\____|\\__,_|_| |_| |_|\\___|
         / _ \\__   _____ _ __| |
        | | | \\ \\ / / _ \\ '__| |
        | |_| |\\ V /  __/ |  |_|
         \\___/  \\_/ \\___|_|  (_)
        """ + text_colors.WHITE
        )


def hangman_lives(lives):
    """
    Displays hangman graphic based on lives left
    """
    lives_left = [
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """,
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        /
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |         |
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |
        ========
        """,
        """
        |/
        |
        |
        |
        |
        |
        ========
        """,

        """
        |
        |
        |
        |
        |
        ========
        """,
        """







        """
    ]
    return lives_left[lives]


def hangman_title():
    print(
        """
         _   _                                         _  ___  _
        | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __ / |/ _ \\/ |
        | |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\| | | | | |
        |  _  | (_| | | | | (_| | | | | | | (_| | | | | | |_| | |
        |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|_|\\___/|_|
                            |___/
        """
    )


def game_rules():
    """
    Shows game rules
    """
    print(
        """
        Guess the word by inputting letters.
        If you get a letter wrong you will lose a life
        and the hangman will begin building.
        When you reach 0 lives you will be hanged
        and it is game over!
        """
    )
    main_menu = input(text_colors.YELLOW + "Press enter to return to the main"
                      " menu\n" + text_colors.WHITE)
    print("\n")
    main()


def main():
    """
    Runs the game
    """
    hangman_title()
    print(hangman_lives(0))
    difficulty = initialise_game()
    if difficulty == "default":
        num_lives = 7
    else:
        num_lives = select_difficulty()

    hangman_word = get_random_word()
    play_game(hangman_word, num_lives)


main()
