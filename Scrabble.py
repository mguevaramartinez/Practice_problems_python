#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 19:48:14 2025

@author: monicaguevara
"""

#a)
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updated_Hand = hand.copy()
   
    for i in word:
        if i in updated_Hand: 
            updated_Hand[i] -= 1
            if updated_Hand[i] == 0:
                del updated_Hand[i] 
    return updated_Hand

#b)

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    updated_Hand = hand.copy()
    eval = []
    if word not in wordList:
        return False
    else:
        for i in word:
            if i in updated_Hand: 
                updated_Hand[i] -= 1
                eval.append(True)
                if updated_Hand[i] == 0:
                      del updated_Hand[i] 
            else: 
                eval.append(False)
            
        return all(eval)


#c)
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    leng = 0
    for i in hand:
        leng += hand[i]
    return leng