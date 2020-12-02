from gamescards.CardGame import CardGame
game = CardGame()
game.player1.show()
game.player2.show()
for i in range(10):
    c1 = game.player1.get_card()
    c2 = game.player2.get_card()
    print(f"{game.player1.name}---{c1}")
    print(f"{game.player2.name}---{c2}")
    if (c1 > c2) is True:
        game.player2.add_card(c1)
        game.player2.add_card(c2)
        print(f"{game.player1.name} won!")
    if (c1 > c2) is False:
        game.player1.add_card(c1)
        game.player1.add_card(c2)
        print(f"{game.player2.name} won!")
game.get_winner()