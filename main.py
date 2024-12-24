from model.blackjack import Blackjack

def main():
    deckCount = 6
    game = Blackjack(deckCount)
    game.run()

if __name__ == "__main__":
    main()