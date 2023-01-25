hand = input()
clubs = []
diamonds = []
hearts = []
spades = []
pointsclub = 0
pointsdiamond = 0
pointshearts = 0
pointsspades = 0        

for i in range(len(hand)):
    if hand[i] == "D":
        break
    else:
        clubs.append(hand[i])

for i in range(len(clubs), len(hand)):
    if hand[i] == "H":
        break
    else:
        diamonds.append(hand[i])

for i in range(len(clubs) + len(diamonds), len(hand)):
    if hand[i] == "S":
        break
    else:
        hearts.append(hand[i])

for i in range(len(clubs) + len(diamonds) + len(hearts), len(hand)):
    spades.append(hand[i])

for i in range(len(clubs)):
    if clubs[i] == "A":
        pointsclub += 4
    elif clubs[i] == "K":
        pointsclub += 3
    elif clubs[i] == "Q":
        pointsclub += 2
    elif clubs[i] == "J":
        pointsclub += 1
    elif len(clubs) == 1:
        pointsclub += 3
    elif len(clubs) == 2:
        pointsclub += 2
    elif len(clubs) == 3:
        pointsclub += 1

for i in range(len(diamonds)):
    if diamonds[i] == "A":
        pointsdiamond += 4
    elif diamonds[i] == "K":
        pointsdiamond += 3
    elif diamonds[i] == "Q":
        pointsdiamond += 2
    elif diamonds[i] == "J":
        pointsdiamond += 1
    elif len(diamonds) == 1:
        pointsdiamond += 3
    elif len(diamonds) == 2:
        pointsdiamond += 2
    elif len(diamonds) == 3:
        pointsdiamond += 1

for i in range(len(hearts)):
    if hearts[i] == "A":
        pointshearts += 4
    elif hearts[i] == "K":
        pointshearts += 3
    elif hearts[i] == "Q":
        pointshearts += 2
    elif hearts[i] == "J":
        pointshearts += 1
    elif len(hearts) == 1:
        pointshearts += 3
    elif len(hearts) == 2:
        pointshearts += 2
    elif len(hearts) == 3:
        pointshearts += 1

for i in range(len(spades)):
    if spades[i] == "A":
        pointsspades += 4
    elif spades[i] == "K":
        pointsspades += 3
    elif spades[i] == "Q":
        pointsspades += 2
    elif spades[i] == "J":
        pointsspades += 1
    elif len(spades) == 1:
        pointsspades += 3
    elif len(spades) == 2:
        pointsspades += 2
    elif len(spades) == 3:
        pointsspades += 1

print("Cards Dealt              Points")

