from deck import Deck

class Blackjack:

    def __init__(self, deck, table):
        self.table = table
        self.deck = deck

    @classmethod
    def cardEval(cls, count):
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

        print("The dealer is showing a", Deck.printCard(dealerHand[0]))
        print()
        print("You have", Deck.printCard(playerHand[0]), "and", Deck.printCard(playerHand[1]))
        print()
        playerCount = Deck.cardVal(playerHand[0]) + Deck.cardVal(playerHand[1])

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
                    print("You have", Deck.printCard(playerHand[0]), "and", Deck.printCard(playerHand[1]), "and", Deck.printCard(playerHand[len(playerHand) - 1]))
                    print()
                    playerCount += Deck.cardVal(playerHand[len(playerHand) - 1])
                    val = Blackjack.cardEval(playerCount)
                    if val == 1:
                        continue
                    else:
                        break
                break
            elif move == "S":
                break
            elif move == "D":
                # double bet logic
                playerHand.append(self.deck.dealCard())
                playerVal += Deck.cardVal(playerHand[2])
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
