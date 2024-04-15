import random


def dice_game():
    global high_score
    high_score = 0
    while True:
        print("Current  High Score: ", high_score)
        val = input("1) Roll Dice\n2) Leave Game\nEnter your choice: ")
        val = val.strip()
        if val == "1":
            i = 2
            sum = 0
            print("\n")
            while i > 0:
                val1 = random.randint(1, 6)
                print("You roll a... ", val1)
                sum = sum + val1
                i = i-1
            print("\nYou have rolled a total of:", sum)
            if (sum > high_score):
                print("\nNew high score!\n")
                high_score = sum
        elif val == "2":
            print("Goodbye!")
            print("Your highscore was ", high_score)
            break
        else:
            print("\nIncorrect Selection")


dice_game()
