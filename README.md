# My first Practice_problems_python

Problems to practice programming in python. 
There are three problems in this folder:

**1. Monthly payment**
This problems determines the minimum monthly payment needed to pay off a credit card balance in 12 months using different methods:

a) First Section:
	•	Iterates over 12 months applying minimum monthly payments (based on monthlyPaymentRate).
	•	Computes remaining balance after interest accrues.

b) Second Section (Brute Force Method):
	•	Starts with a minimum payment of $10 and increases by $10 each iteration.
	•	Checks if the balance is paid off within 12 months.
	•	Keeps increasing the payment until balance reaches zero or less.

c) Third Section (Bisection Search - Efficient Method):
	•	Uses binary search between lower and upper bounds of the possible monthly payment.
	•	Iteratively narrows down the optimal payment to reduce balance to zero within 12 months.
	•	Faster than brute force because it halves the search space each iteration.

**2. Hangman**

Breakdown of Functions

a) isWordGuessed(secretWord, lettersGuessed)
	•	Checks if all letters of the secret word have been guessed.
	•	Returns True if guessed correctly, False otherwise.

b) getGuessedWord(secretWord, lettersGuessed)
	•	Returns a string representation of the guessed word so far.
	•	Replaces unguessed letters with underscores (_).

c) getAvailableLetters(lettersGuessed)
	•	Returns a string of remaining letters that haven’t been guessed.

d) hangman(secretWord)
	•	Runs the game loop until the player guesses the word or runs out of attempts.
	•	Displays information about:
	•	Remaining guesses
	•	Available letters
	•	Current guessed word state
	•	Handles repeated guesses & updates the game state.

 **3. Scrabble**
 Breakdown of Functions

a) getWordScore(word, n)
	•	Calculates the score for a word based on Scrabble letter values (SCRABBLE_LETTER_VALUES).
	•	Score = sum of letter values × word length.
	•	If the word uses all n letters, an extra 50 points is awarded.

b) updateHand(hand, word)
	•	Removes letters used in a word from the player’s hand.
	•	Returns an updated hand dictionary without modifying the original hand.

c) isValidWord(word, hand, wordList)
	•	Checks if the word exists in the dictionary (wordList).
	•	Ensures the word can be formed using available letters in hand.
	•	Returns True if valid, False otherwise.

d) calculateHandlen(hand)
	•	Returns the total number of letters remaining in the player’s hand.
