from gamescards.CardGame import CardGame
a = CardGame()
a.player1.show()
a.player2.show()
for i in range(10):
    c1 = a.player1.get_card()
    c2 = a.player2.get_card()
    print(f"{a.player1.name}---{c1}")
    print(f"{a.player2.name}---{c2}")
    if (c1 > c2) is True:
        a.player2.add_card(c1)
        a.player2.add_card(c2)
        print(f"{a.player1.name} won!")
    if (c1 > c2) is False:
        a.player1.add_card(c1)
        a.player1.add_card(c2)
        print(f"{a.player2.name} won!")
a.get_winner()