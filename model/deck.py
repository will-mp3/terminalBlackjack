import random

class Deck:
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    CARDS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, deckCount = 2):
        self.deckCount = deckCount
        self.deck = [(card, suit) for card in Deck.CARDS for suit in Deck.SUITS] * self.deckCount

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def dealCard(self):
        val = random.randint(0, 51 * self.deckCount)
        card = self.deck[val]
        self.deck.remove(card)
        return card

    
def main():
    deck = Deck()
    deck.shuffleDeck()
    card = deck.dealCard()
    print(card)
    print(Deck.cardVal(card))
    print(Deck.printCard(card))

if __name__ == "__main__":
    main()
