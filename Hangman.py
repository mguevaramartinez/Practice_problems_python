#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 19:45:17 2025

@author: monicaguevara
"""

#a)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
 
    answer = ''
    for i in secretWord:
        if i in lettersGuessed:
            answer = True
        else:
            answer = False
            break
    return answer

#b)

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    palabra = []
    for i in secretWord:
        if i in lettersGuessed:
            palabra.append(i)
        else:
            palabra.append('_ ')
    hang = ''.join(palabra)
    return hang
            

#c
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string 
    all_letters = 'abcdefghijklmnopqrstuvwxyz'
    remaining_letters = list(all_letters)
    for i in lettersGuessed:
        if i in all_letters:
            remaining_letters.remove(i)
    remaining_letters = ''.join(remaining_letters)
    return remaining_letters


# d)
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    number_of_guesses = 8
    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    guessedWord = getGuessedWord(secretWord, lettersGuessed)
    are_we_done = isWordGuessed(secretWord, lettersGuessed)
    
  
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    while number_of_guesses > 0 and are_we_done == False:    
        print('-------------')
        print('You have', number_of_guesses, 'guesses left.')
        print('Available letters:', availableLetters)
        guess = input('Please guess a letter: ')
        guessInLowerCase = guess.lower()  
        while guessInLowerCase in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            print('You have', number_of_guesses, 'guesses left.')
            print('Available letters:', availableLetters)   
            guess = input('Please guess a letter: ')
            guessInLowerCase = guess.lower() 
        lettersGuessed.append(guessInLowerCase)
        availableLetters = getAvailableLetters(lettersGuessed) 
        if guessInLowerCase in secretWord:      
            print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
        else:
            number_of_guesses -=1 
            print('Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed))
        are_we_done = isWordGuessed(secretWord, lettersGuessed)
    if are_we_done == True:
        print('-------------')
        print('Congratulations, you won!')
    else:
        print('-----------', '\n')
        print('Sorry, you ran out of guesses. The word was ', secretWord)


