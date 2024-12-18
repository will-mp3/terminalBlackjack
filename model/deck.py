import random

class Deck:
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    CARDS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, deckCount):
        self.deckCount = deckCount
        self.deck = [(card, suit) for card in Deck.CARDS for suit in Deck.SUITS] * self.deckCount

    def cardVal(self, card):
        if card[0] in ['Jack', 'Queen', 'King']:
            return 10
        elif card[0] == 'Ace':
            return 11
        else:
            return int(card[0])

    def shuffleDeck(self):
        random.shuffle(self.deck)