from gamescards.DeckOfCards import DeckOfCards
from random import *


class Player:

    deck = DeckOfCards()
    lst = deck.lst_cards

    def __init__(self, name):
        self.name = name
        self.deck = DeckOfCards()
        self.player_hand = []

    def set_hand(self, num_cards=10):
        for i in range(num_cards):
            x = self.lst.pop(randint(0, len(self.lst)-1))
            self.player_hand.append(x)

    def get_card(self):
        card = self.player_hand.pop(randint(0, len(self.player_hand)-1))
        return card

    def add_card(self, card):
        self.player_hand.append(card)

    def show(self):
        print(f"{self.name}---Hand:{self.player_hand}")





