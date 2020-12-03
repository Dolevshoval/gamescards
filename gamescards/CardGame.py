from gamescards.Player import Player


class CardGame:
    def __init__(self):
        self.player1 = Player("Dolev")
        self.player2 = Player("Shay")
        self.num_of_cards = 10
        self.new_game()

    def new_game(self):
        self.player1.set_hand(self.num_of_cards)
        self.player2.set_hand(self.num_of_cards)

    def get_winner(self):
        if len(self.player1.player_hand) > len(self.player2.player_hand):
            print(f"{self.player2.name} won the game!")
        if len(self.player1.player_hand) < len(self.player2.player_hand):
            print(f"{self.player1.name} won the game!")
        if len(self.player1.player_hand) == len(self.player2.player_hand):
            print(None)



