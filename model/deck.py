import random
from .card import Card

class Deck:
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    CARDS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, deckCount = 2):
        self.deckCount = deckCount
        self.deck = [Card(card, suit) for card in Deck.CARDS for suit in Deck.SUITS] * self.deckCount

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def dealCard(self):
        val = random.randint(0, len(self.deck) - 1)
        card = self.deck[val]
        self.deck.remove(card)
        return card
