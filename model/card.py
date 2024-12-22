class Card:
    def __init__(self, card, suit):
        self.card = card
        self.suit = suit

    def getVal(self):
        if self.card in ['Jack', 'Queen', 'King']:
            return 10
        elif self.card == 'Ace':
            return 11
        else:
            return int(self.card)

    def printCard(self):
        return str(self.card) + " of " + str(self.suit)