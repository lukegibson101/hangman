### **Bugs**

## **Fixed Bugs**
* Bug: When implementing hangman graphics, lives left did not correspond to amount of stages left in hangman.
  * Fix: Due to lists iterating from 0, set lives displayed to user as lives + 1 and also adjusted the game over setting for lives >=0
* Bug: When testing hangman graphics, the bottom graphic was shifted over to the right.
  * Fix: Replaced \ with double \\\\ make \ print to the terminal. 


### **Resources**
 * [Random Word Generator](https://www.randomlists.com/random-words) - to generate a random word for the game. 