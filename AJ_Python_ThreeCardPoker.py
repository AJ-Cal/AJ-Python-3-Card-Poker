# Goal: create a virtual three card poker game 
# Requirement:
# 1) Create a class to define objects
# 2) Create cards and see the cards 
# 3) Know the total number of players
# 4) Distribute three cards randomly


import random
cards = []
class Card:
    handNumber = 0
    def __init__(self,suit,number,):
        self.suit = suit
        self.number = number
    def printInfo(self):
        print(f'{self.suit}{self.number}') 

class cardMaker(Card):
    def init__(self,name):
        self.name = name
    def makeCard(self):
        cardCreator = 0
        numberGenerator = 0
        suit = ''
        for i in range(1, 14): 
            numberGenerator = i
            if numberGenerator == 1:
                numberGenerator = 'A'
            elif numberGenerator == 11:
                numberGenerator = 'J'
            elif numberGenerator == 12:
                numberGenerator = 'Q'
            elif numberGenerator == 13:
                numberGenerator = 'K'
            for i in range(0, 4):
                cardCreator = i
                if cardCreator == 0:
                    suit = '\u2665' #hearts
                elif cardCreator == 1:
                    suit = '\u2663' #clubs
                elif cardCreator == 2: 
                    suit = '\u2666' #diamonds
                else:
                    suit = '\u2660' #spades
                card = Card(suit, numberGenerator)
                cards.append(card)
                if len(cards) == 52:
                    break
        random.shuffle(cards)
        
cardMake = cardMaker('MakeCards', 7)
cardMake.makeCard() 


class Player(cardMaker):
    def __init__(self, name):
        self.name = name 
    def getHand(self):
        hand = []
        while len(hand) < 3:
            for i in cards:
                hand.append(i)
                cards.remove(i)
                if len(hand) == 3:
                    break
        for card in hand:
            card.printInfo()
class Amti(cardMaker):
    def __init__(self,name):
        self.name = name
    def playerMaker(self):
        makePlayers = int(input('How many other players would you like there to be? '))
        playerMaker = 0
        for i in range(playerMaker, makePlayers):
            player = Player(i)
            print(f"This is player {i + 1}'s hand.")
            player.getHand()
        you = Player('you')
        print('This is your hand.')
        you.getHand()

            
amti = Amti('Amti')
amti.playerMaker()
