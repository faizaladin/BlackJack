#blackjack class

#import PlayingCard / Deck class / Button class --> change file names
#from ____ import*

from Deck import *
from PlayingCard import *
from graphics import *
from Button import *

class Blackjack:
    """Blackjack class is used to combine the Deck, PlayingCard, and Button class
        to implement a game of BlackJack."""
    """ When program is run user (player) is presented with graphic window: with 2 randomized
        cards for dealer and player, one card from each player is hidden.
        Once player clicks "hit" their second card is revealed and current total is added up.
        If user decides to pick another card - click "hit" - and another card is dealt to player.
        Once player decides to stop picking card - click "Stay" - and program will reveal Dealer's
        cards and whether or not player won, lose, or drawed.
        Players can play again by clicking "new game" - this will re-run the program"""
    def __init__(self, dHand=[], pHand=[]):
        """Constructor for initializing the instance variables
            and gives playingDeck an initial shuffle"""
        #dealerHand : a list of PlayingCard objects to represent the dealer's hand
        self.dealerHand = dHand=[]
        #playerHand : a list of PlayingCard objects to represent the player's hand
        self.playerHand= pHand=[]
        #deck object representing the deck of cards used in game
        self.playingDeck = Deck()
        #gives playingDeck an initial shuffle
        self.playingDeck.shuffle()
        #makes a list for card objects
        self.visiblecards = []

    def initDeal(self, gwin, xposD, yposD, xposP, yposP):
        """Dealing initial cards, 2 cards per player displayed on graphic
            win: displays 1 card,while 1 card is faced down.
            Until user finishes his/her turn the dealer's cards are revealed.
            xposD and yposD give the initial position of dealer cards,
            xposP and yposP are similar"""
        #from Deck class cards chosen and removed from card deck - for both dealer and player
        self.dealerHand = [self.playingDeck.dealCard()]
        self.playerHand = [self.playingDeck.dealCard(), self.playingDeck.dealCard()]
        #importing image of cards from folder. 
        self.card1 = Image(Point(xposP, yposP), f'playingcards/{self.playerHand[0]}.gif')
        self.card2 = Image(Point(xposP + 100, yposP), f'playingcards/{self.playerHand[1]}.gif')
        self.card3 = Image(Point(xposD, yposD), f'playingcards/{self.dealerHand[0]}.gif')
        self.card4 = Image(Point(xposD + 100, yposD), f'playingcards/b2fv.gif')
        #card images are stored in a list to be undrawn with the new game function
        self.visiblecards = [self.card1, self.card2, self.card3, self.card4]
        #cards are drawn
        self.card1.draw(gwin)
        self.card2.draw(gwin)
        self.card3.draw(gwin)
        self.card4.draw(gwin)

    def hit(self, gwin, xPos, yPos):
        """ this method adds a new card to the player's hand
        placing it as xPos and yPos"""
        self.playerHand.append(self.playingDeck.dealCard())
        self.card = Image(Point(xPos, yPos), f'playingcards/{self.playerHand[len(self.playerHand)-1]}.gif')
        #card image is added 
        self.visiblecards.append(self.card)
        self.card.draw(gwin)

    def getplayerHand(self):
        """returns the players hand """
        return self.playerHand

    def getdealerHand(self):
        """returns the dealer's hand """
        return self.dealerHand

    def evaluateHand(self, hand):
        """ accumulates the total cards in the hand and returns the total.
        using for loop and if statements to determine value of ace and picture cards"""
        counter = 0
        hasAce = 0
        #using for loop...... 
        for i in range(len(hand)):
            #evaluating ace card 
            if hand[i].getRank() == 1:
                hasAce = hasAce + 1
                counter = counter +  11
            #picture cards
            elif hand[i].getRank() == 11 or hand[i].getRank() == 12 or hand[i].getRank() == 13:
                #picture cards = 10, if dealt a value of 10 will be added to total score
                counter = counter + 10
            else:
                counter = counter + hand[i].getRank()
        #if total is already over 21, ace is counted as 1
        while counter > 21 and hasAce > 0:
            counter = counter - 10
            hasAce = hasAce - 1       
        return counter

    def dealerPlays(self, gwin, xPos, yPos):
        """ dealer deals cards for his/herself"""
        self.dealerHand.append(self.playingDeck.dealCard())
        #import and draw card image from folder
        self.card = Image(Point(xPos, yPos), f'playingcards/{self.dealerHand[len(self.dealerHand)-1]}.gif')
        self.visiblecards.append(self.card)
        #adds card image to visible cards list
        self.card.draw(gwin)

    def bust(self, hand):
        """returns result of card total whether user busts or not"""
        if self.evaluateHand(hand) > 21:
            return True
        else:
            return False

    def undraw(self, gwin):
        #goes through the list of card images and removes them from the table
        #wipes cards from table for new game
        for i in range(len(self.visiblecards)):
            self.visiblecards[i].undraw()
        
        
#sample program does not implement the feature of dealing the first dealer card face down

#testing class
def main():
    #calling methods and classes
    deck = Deck()
    deck.shuffle()
    playerhand = [deck.dealCard(), deck.dealCard()]
    dealerhand = [deck.dealCard()]
    game = Blackjack(dealerhand, playerhand)
    #creating the graphic window
    win = GraphWin("Blackjack", 800, 600)
    #buttons, from button class
    hitButton = Button(win, Point(250,270), 150, 45, "Hit")
    standButton = Button(win, Point(450,270), 150, 45, "Stand")
    quitButton = Button(win, Point(250,530), 150, 45, "Quit")
    newButton = Button(win, Point(450,530), 150, 45, "New Game")
    dealerText = Text(Point(100,100), "Dealer")
    dealerText.setSize(15)
    dealerText.draw(win)
    #labels 
    playerText = Text(Point(100,400), "Player")
    playerText.setSize(15)
    playerText.draw(win)
    game.initDeal(win, 210, 100, 210, 400)
    #total score 
    playerTotal = Text(Point(100,425), f'Total: {game.evaluateHand(game.getplayerHand())}')
    playerTotal.setSize(15)
    playerTotal.draw(win)
    dealerTotal = Text(Point(100,125), f'Total: {game.evaluateHand(game.getdealerHand())}')
    dealerTotal.setSize(15)
    dealerTotal.draw(win)
    hitButton.activate()
    standButton.activate()
    pt = win.getMouse()

     #if statements to run methods and evaluate whether player wins, loses, or draws with dealer.

    while not quitButton.clicked(pt):
        if hitButton.clicked(pt):
            #if user presses the hit button
            game.hit(win, 210 + ((len(game.getplayerHand()))*100), 400)
            playerTotal.setText(f'Total: {game.evaluateHand(game.getplayerHand())}')
            #adds another card to the table in the players hand
            #updates the total for the player
            if game.bust(game.getplayerHand()):
                #checks to see if the player's total goes over 21
                hitButton.deactivate()
                standButton.deactivate()
                #both buttons deactivate to make sure user cannot keep using them after game ends
                quitButton.activate()
                newButton.activate()
                #bolds the newgame button and the quit button for user to see and pick
                gameoverText = Text(Point(400,200), "Game Over. You Busted. Dealer Wins.")
                gameoverText.setSize(20)
                gameoverText.setTextColor('red')
                gameoverText.draw(win)
                #displays game over text telling the user they lost

        if standButton.clicked(pt):
            #if user hits the stand button
            hitButton.deactivate()
            standButton.deactivate()
            #both buttons deactivate to make sure user cannot keep using them after game ends
            quitButton.activate()
            newButton.activate()
            while game.evaluateHand(game.getdealerHand()) < 17 and game.bust(game.getdealerHand()) == False:
                game.dealerPlays(win, 210 + ((len(game.getdealerHand()))*100), 100)
                dealerTotal.setText(f'Total: {game.evaluateHand(game.getdealerHand())}')
                #if the dealer has less than 17, the dealer will keep taking cards until they bust or go over 17
                #dealer's total updates as they add cards to their hand

            if game.evaluateHand(game.getplayerHand()) > game.evaluateHand(game.getdealerHand()) or game.bust(game.getdealerHand()) == True:
                gameoverText = Text(Point(400,200), "You Win!")
                gameoverText.setSize(20)
                gameoverText.setTextColor('green')
                gameoverText.draw(win)
                #if dealer has a smaller total than the user, text displays saying the user won

            elif game.evaluateHand(game.getplayerHand()) == game.evaluateHand(game.getdealerHand()):
                gameoverText = Text(Point(400,200), "It's a draw...")
                gameoverText.setSize(20)
                gameoverText.setTextColor('blue')
                gameoverText.draw(win)
                #if the dealer and player have the same total, text displays the game is a draw

            else:
                gameoverText = Text(Point(400,200), "Game Over. Dealer Wins.")
                gameoverText.setSize(20)
                gameoverText.setTextColor('red')
                gameoverText.draw(win)
                #if dealer has a larger total, text displays the dealer won


        if newButton.clicked(pt):
            game.undraw(win)
            #all cards are taken off the table 
            game.initDeal(win, 210, 100, 210, 400)
            #new cards are dealt
            gameoverText.undraw()
            #game over text is undrawn for new game
            playerTotal.setText(f'Total: {game.evaluateHand(game.getplayerHand())}')
            dealerTotal.setText(f'Total: {game.evaluateHand(game.getdealerHand())}')
            #totals are updated for the new cards
            hitButton.activate()
            standButton.activate()
            #buttons are reactivated for new gamee
            

        pt = win.getMouse()
        #gets mouse click again for the while loop
   
    win.close() 

main()
    
