from .deck import Deck
from .card import Card

class Blackjack:

    def __init__(self, deckCount):
        self.deckCount = deckCount
        self.deck = Deck(self.deckCount)
        self.dealerHand, self.playerHand = [], []
        self.playerCount = 0
        self.dealerCount = 0
        self.playerChips = 100

    def _clear(self):
        self.deck = Deck(self.deckCount)
        self.dealerHand, self.playerHand = [], []
        self.playerCount = 0
        self.dealerCount = 0

    def _getCount(self, person):
        count = 0
        hasAce = False

        if person == "p":
            for card in self.playerHand:
                if card.card in ['Jack', 'Queen', 'King']:
                    count += 10
                elif card.card == 'Ace':
                    hasAce = True
                    count += 11
                else:
                    count += int(card.card)
            
            if count > 21 and hasAce:
                count -= 10
        
            return count

        if person == "d":
            for card in self.dealerHand:
                if card.card in ['Jack', 'Queen', 'King']:
                    count += 10
                elif card.card == 'Ace':
                    hasAce = True
                    count += 11
                else:
                    count += int(card.card)
            
            if count > 21 and hasAce:
                count -= 10
        
            return count


    def _playAgain(self):

        if self.playerChips == 0:
            print("Out of chips.")
            return
        print("Player has", self.playerChips, "chips remaining.")
        print()
        choice = input("Would you like to play again? (Y/N) ")
        print()
        if choice == "Y":
            self.run()
        elif choice == "N":
            return False
        else:
            print("Invalid input.")
            self._playAgain()

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
            print("Blackjack! You win.")
            return True
        else:
            return False
            
    def _hit(self):

        self.playerHand.append(self.deck.dealCard())

        print("You have", self.playerHand[0].printCard() + ",", self.playerHand[1].printCard(), end="")

        for i in range(len(self.playerHand) - 2): # prints the third card onward
            print(",", self.playerHand[2 + i].printCard(), end="")
        print()

        self.playerCount = self._getCount("p")
                    
        val = self._cardEval()

        return val

    def _dealerHit(self):
        self.dealerHand.append(self.deck.dealCard())

        print("Dealer showing", self.dealerHand[0].printCard() + ",", self.dealerHand[1].printCard(), end="")

        for i in range(len(self.dealerHand) - 2): # prints the third card onward
            print(",", self.dealerHand[2 + i].printCard(), end="")
        print()

        self.dealerCount = self._getCount("d")

    def run(self):
        self._clear()

        print()
        print("You have", self.playerChips, "chips")
        print()

        self.deck.shuffleDeck()
        print("Welcome to the table! Please take a seat and place your bets.")
        print()
        while 1:
            bet = input("BET AMOUNT: ")
            print()
            bet = int(bet)
            if bet <= self.playerChips:
                break
            else:
                print("Invalid bet amount.")
                print()
                continue

        # deal cards, in this order
        self.playerHand.append(self.deck.dealCard())
        self.dealerHand.append(self.deck.dealCard())
        self.playerHand.append(self.deck.dealCard())
        self.dealerHand.append(self.deck.dealCard())

        print("The dealer is showing a", self.dealerHand[0].printCard())
        print()
        print("You have", self.playerHand[0].printCard() + ",", self.playerHand[1].printCard())
        self.playerCount = self._getCount("p")
        self.dealerCount = self._getCount("d")

        if self._checkBJ():
            playerChips += bet * 1.5
            choice = self._playAgain()
            if not choice:
                return

        # hit or stand logic
        while 1:
            print()
            move = input("Would you like to hit, stand, or double: (H/S/D) ")
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
                if (bet * 2) <= self.playerChips:
                    bet = bet * 2
                    self.playerHand.append(self.deck.dealCard())
                    print("You have", self.playerHand[0].printCard() + ",", self.playerHand[1].printCard(), ",", self.playerHand[2].printCard())
                    print()
                    self.playerCount = self._getCount("p")
                    break
            else:
                print("Invalid response, please respond again.")
                print()
        
        if self.playerCount > 21:
            self.playerChips -= bet
            self._playAgain()
        
        if self.dealerCount == 21:
            print("Dealer showing 21. You lose.")
            self.playerChips -= bet
            self._playAgain()
        elif self.dealerCount >= 17:
            if self.dealerCount > self.playerCount:
                print("Dealer showing", self.dealerHand[0].printCard()+ ",", self.dealerHand[1].printCard() + ". You lose.")
                print()
                self.playerChips -= bet
                self._playAgain()
            elif self.dealerCount < self.playerCount:
                print("Dealer showing", self.dealerHand[0].printCard()+ ",", self.dealerHand[1].printCard() + ". You win!")
                print()
                self.playerChips += bet
                self._playAgain()
            else:
                print("Dealer showing", self.dealerHand[0].printCard()+ ",", self.dealerHand[1].printCard() + ". Push.")
                print()
                self._playAgain()
        else:
            print("Dealer showing", self.dealerHand[0].printCard()+ ",", self.dealerHand[1].printCard())
            print()
            while self.dealerCount <= 17:
                self._dealerHit()
                if self.dealerCount > 21:
                    print()
                    print("You win!")
                    self.playerChips += bet
                    self._playAgain()
                elif self.dealerCount < 21 and self.dealerCount >= 17 and self.dealerCount > self.playerCount: 
                    print()
                    print("You lose.")
                    self.playerChips -= bet
                    self._playAgain()
                elif self.dealerCount < 21 and self.dealerCount >= 17 and self.dealerCount < self.playerCount:
                    print()
                    print("You win!")
                    self.playerChips += bet
                    self._playAgain()
                else:
                    continue