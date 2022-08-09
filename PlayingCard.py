#Faiz Aladin and Christine Vuu
#November 4th, 2020
#PA 5
#PlayingCard class adapted from programming exercise 11 - chapter 10

import random

class PlayingCard:
    """ This class is where the numeric rank and suit values are stored"""

    def __init__(self, rank, suit):
        """ constructor to define instance variables which
            can be accessed from any of the methods in class"""
        #rank: integar to indicate the ranks of cards (1-13)
        #sets rank equal to a list containing int of each rank
        self.rank = rank
        #suit: to indicate the card suit:(diamonds, clubs, hearts or spades)
        #sets suit equal to a list containing the names of each suit
        self.suit = suit
        
    def __str__(self):
        """converting object into a string, returns card name"""
        n = self.rank
        if self.suit == 'D':
            s = "d"
        elif self.suit =='S':
            s = "s"
        elif self.suit == 'H':
            s = "h"
        else:
            s = "c"
        #each possible card is represented by a integar 
        rank = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

        self.cardname = (f'{s}{rank[n-1]}')
        return self.cardname

    def getRank(self):
        """returns the rank of the card"""
        return self.rank

    def getSuit(self):
        """returns the suit of the card"""
        return self.suit
    
