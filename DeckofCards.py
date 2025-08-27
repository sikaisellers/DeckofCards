import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.deck = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, num_cards):
        dealt_cards = []
        for _ in range(num_cards):
            if self.deck:
                dealt_cards.append(self.deck.pop())
        return dealt_cards

    def count(self):
        return len(self.deck)

def main():
    print("Welcome to the Card Dealer!\n")
    deck = Deck()
    deck.shuffle()
    print(f"Deck shuffled. Total cards: {deck.count()}")

    try:
        num = int(input("How many cards would you like to be dealt? "))
        if num <= 0:
            print("Please enter a positive number.")
            return
        if num > deck.count():
            print(f"Only {deck.count()} cards left in the deck.")
            return

        print("\nDealing cards...\n")
        hand = deck.deal(num)
        for card in hand:
            print(card)

        print(f"\nCards remaining in deck: {deck.count()}")
        print("Good luck!")

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
