#Faiz Aladin and Christine Vuu
#November 4th, 2020
#PA 5
#Deck class adapted from programming exercise 15 - chapter 11

import random
from PlayingCard import *
class Deck:
    """ This class is used to represent a deck of cards, pool of cards finite"""
    def __init__(self):
        """ Constructor to create a deck of 52 cards """
        #using initials to represent card suits
        suit = ['C','D','H','S']

        #empty list - too append and build method to create deck
        cardSpecs = []
        #nested loop
        for i in range(52):
            x = i % 13 +1 #13 possible ranks
            y = suit [i % 4]  #4 possible suits
            cardSpecs.append((x,y))
        self.cards = []
        for (x,y) in cardSpecs:
            #appending cards to the attriubute list
            self.cards.append(PlayingCard(x,y))
    #Methods
    def shuffle(self):
        """ Randomizes the order of the cards """
        random.shuffle(self.cards)

    def dealCard(self):
        """ Returns a single card from the top of the deck and removes
            the card from the deck"""
        #pop() removes the last card from the top of the deck and returns that card
        return self.cards.pop(0)

    def cardsLeft(self):
        """ Returns remaining number of cards from deck""" 
        return len(self.cards)

#main function to test class, using for loop
def main():
    deck = Deck()
    deck.shuffle()
    for i in range(52):
        print(deck.dealCard())

if __name__=='__main__':
    main()
    
    

        
        
