from deck import Deck
from card import Card

class Blackjack:

    def __init__(self, deck, table):
        self.table = table
        self.deck = deck
        self.dealerHand, self.playerHand = [], []
        self.playerCount = 0

    def _cardEval(self):
        
        if self.playerCount <= 21:
            return True
        else:
            print()
            print("Player bust.")
            print()
            return False

    def _checkBJ(self):

        if self.playerCount == 21:
            return True
        else:
            return False
            
    def _hit(self):

        self.playerHand.append(self.deck.dealCard())

        print("You have", self.playerHand[0].printCard() + ",", self.playerHand[1].printCard(), end="")

        for i in range(len(self.playerHand) - 2): # prints the third card onward
            print(",", self.playerHand[2 + i].printCard(), end="")
        print()

        self.playerCount += self.playerHand[len(self.playerHand) - 1].getVal()
                    
        val = self._cardEval()

        return val

    def run(self):

        self.deck.shuffleDeck()
        print("Welcome to the table! Please take a seat and place your bets.")
        print()

        # deal cards, in this order
        self.playerHand.append(self.deck.dealCard())
        self.dealerHand.append(self.deck.dealCard())
        self.playerHand.append(self.deck.dealCard())
        self.dealerHand.append(self.deck.dealCard())

        print("The dealer is showing a", self.dealerHand[0].printCard())
        print()
        print("You have", self.playerHand[0].printCard() + ",", self.playerHand[1].printCard())
        print()
        self.playerCount = self.playerHand[0].getVal() + self.playerHand[1].getVal()

        if self._checkBJ():
            return

        # hit or stand logic
        while 1:
            move = input("Would you like to hit, stand, or double: (H/S/D)")
            print()
            if move == "H":
                val = self._hit()
                if val:
                    continue
                else:
                    break

            elif move == "S":
                break

            elif move == "D":
                # double bet logic
                self.playerHand.append(self.deck.dealCard())
                playerVal += self.playerHand[2].getVal()
                break
            else:
                print("Invalid response, please respond again.")
                print()

def main():
    deck = Deck()
    game = Blackjack(deck, "NULL")
    game.run()

if __name__ == "__main__":
    main() 
