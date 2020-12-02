from gamescards.Cards import Cards
from random import *


class DeckOfCards:  # make a new deck_cards

    def __init__(self):
        self.suit = ["Diamond", "Spade", "Heart", "Club"]
        self.value = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        self.lst_cards = []
        self.volume = 0
        for i in self.value:
            for z in self.suit:
                self.card = Cards(i, z, self.volume)
                self.lst_cards += [self.card]
                self.volume += 1

    def shuffle(self):
        shuffle(self.lst_cards)

    def deal_one(self):
        x = choice(self.lst_cards)
        self.lst_cards.remove(x)
        return x

    def show(self):
        print(f"the deck is: {self.lst_cards}")




