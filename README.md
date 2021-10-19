# **Hangman101**
Hangman101 is a Python terminal game, which runs on the Code Institute mock terminal on Heroku.
Users can try to guess the word by inputting letters until they either guess the word or it is game over. 

[Hangman101](https://hangman101.herokuapp.com/) - You can view the live site here. 




### **Bugs**

## **Fixed Bugs**
* Bug: When implementing hangman graphics, lives left did not correspond to amount of stages left in hangman.
  * Fix: Due to lists iterating from 0, set lives displayed to user as lives + 1 and also adjusted the game over setting for lives >=0
* Bug: When testing hangman graphics, the bottom graphic was shifted over to the right.
  * Fix: Replaced \ with double \\\\ make \ print to the terminal. 
* Bug: When on last life, letters guessed and amount of lives fail to show on terminal.
  * Fix: Set lives to lives >=0 at end of while loop to ensure messages display correctly.
* Bug: Hangman graphic not displaying on game over.
  * Fix: Add in additional stage of hangman graphic. Remove lives + 1 from script, set game over criteria back lives > 0. A more elgant fix for the problem above.
* Bug: When selecting view rules. After returning to the main window, if you selected play game it would go to the difficulty menu
  * Fix: Called main() in game rules rather that initialise_game()


### **Resources**
 * [Random Word Generator](https://www.randomlists.com/random-words) - to generate a random list of 500 words for the game.
 * [Python Hang Man tutorial](https://github.com/kiteco/python-youtube-code/tree/master/build-hangman-in-python) - inspiration on how to build a hang man game. Whilst I have attempted to do my own thing, and greatly expand on the initial example, some code may be similar. 
 * [ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Standard&t=Hangman101) - for creating word art for game title and game over screens.