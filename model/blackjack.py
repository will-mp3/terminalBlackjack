from deck import Deck
from card import Card

class Blackjack:

    def __init__(self, deck, table):
        self.table = table
        self.deck = deck

    @staticmethod
    def cardEval(count):
        if count <= 21:
            return 1
        else:
            print("Player bust.")
            print()
            return 0

    def run(self):
        self.deck.shuffleDeck()
        print("Welcome to the table! Please take a seat and place your bets.")
        print()

        # code to place bets
        dealerHand, playerHand = [], []

        # deal cards, in this order
        playerHand.append(self.deck.dealCard())
        dealerHand.append(self.deck.dealCard())
        playerHand.append(self.deck.dealCard())
        dealerHand.append(self.deck.dealCard())

        print("The dealer is showing a", dealerHand[0].printCard())
        print()
        print("You have", playerHand[0].printCard(), "and", playerHand[1].printCard())
        print()
        playerCount = playerHand[0].getVal() + playerHand[1].getVal()

        if playerCount == 21:
            print("Blackjack! You win.")
            print()
            # payout logic

        # hit or stand logic
        while 1:
            move = input("Would you like to hit, stand, or double: (H/S/D)")
            print()
            if move == "H":
                while 1:
                    playerHand.append(self.deck.dealCard())
                    print("You have", playerHand[0].printCard(), "and", playerHand[1].printCard(), "and", playerHand[len(playerHand) - 1].printCard())
                    print()
                    playerCount += playerHand[len(playerHand) - 1].getVal()
                    val = Blackjack.cardEval(playerCount)
                    break
                if val == 1:
                    continue
                else:
                    break
            elif move == "S":
                break
            elif move == "D":
                # double bet logic
                playerHand.append(self.deck.dealCard())
                playerVal += playerHand[2].getVal()
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
