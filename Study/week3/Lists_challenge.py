import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
                  "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    while True:
        userInput = input(
            "Press enter to pick a card, or Q then enter to quit:")
        userInput = userInput.strip()
        if len(userInput) == 0:
            break
        elif userInput.upper() == "Q":
            quit()
        else:
            print("Invalid selection")
    cardPicked = random.choice(diamonds)
    diamonds.remove(cardPicked)
    hand.append(cardPicked)
    print("Your hand:", hand)
    print("Ramaining Cards:", diamonds)

if not diamonds:
    print("There are no more cards to pick")
