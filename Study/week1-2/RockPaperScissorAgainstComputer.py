import random

from my_pkg import myFunctions as mf


def takeUserInput():
    while True:
        playerOption = input(
            "\n Player please select your option. Enter the number/text for the option.\n 1. ROCK \n 2. PAPER \n 3. SCISSOR \n\n")
        playerOption = playerOption.strip()
        if playerOption == "1" or playerOption.upper() == "ROCK":
            playerOption = "ROCK"
            break
        elif playerOption == "2" or playerOption.upper() == "PAPER":
            playerOption = "PAPER"
            break
        elif playerOption == "3" or playerOption.upper() == "SCISSOR":
            playerOption = "SCISSOR"
            break
        else:
            print("\n Please select correct option \n")
    return playerOption


def roundWinner(opt1, opt2):
    if opt1 == "ROCK" and opt2 == "SCISSOR" or opt1 == "SCISSOR" and opt2 == "PAPER" or opt1 == "PAPER" and opt2 == "ROCK":
        return "Win"
    elif opt2 == "ROCK" and opt1 == "SCISSOR" or opt2 == "SCISSOR" and opt1 == "PAPER" or opt2 == "PAPER" and opt1 == "ROCK":
        return "Loss"
    else:
        return "Draw"


x = 0
y = 0
z = 0

playerSelections = []
computerSelections = []
optionList = ["ROCK", "PAPER", "SCISSOR"]

while True:
    # print("\x1b[0;30;43m" +
    #          "\n Welcome to the Game of ROCK-PAPER-SSCISSOR \n"+"\x1b[0m")
    text = "\n Welcome to the Game of ROCK-PAPER-SSCISSOR \n"
    mf.printingTextWithcolor(text, "yellow")
    print("\x1b[0;30;46m"+"Following are the rules of the game:\n"+"1. Game will be consist of 3 rounds\n"+"2. For each round Player will select 1 option out of Rock/Paper/Scissor and the computer will do the same\n" +
          "3. Each round there can 3 outputs Player wins/ Computer wins/ Draw\n"+"4. Winner will be declared at the end of the game depending upon the number of rounds won\n"+"5. Also game will end if first two rounds are won by same player"+"\x1b[0m")

    while x+y+z < 3:
        playerOption = takeUserInput()
        playerSelections.append(playerOption)
        computerOption = random.choice(optionList)
        computerSelections.append(computerOption)

        output = roundWinner(playerOption, computerOption)
        if output == "Win":
            print(playerOption+" beats the "+computerOption)
            print("Player won this round.")
            x = x+1
            if x > 1:
                break
        elif output == "Loss":
            print(computerOption+" beats the "+playerOption)
            print("Computer won this round.")
            y = y+1
            if y > 1:
                break
        else:
            print(playerOption+" matches the "+computerOption)
            print("This round is a draw")
            z = z+1

    print("\n")
    if (x > y):
        print("\x1b[6;30;42m"+"Player is the winner of the game\n"+"\x1b[0m")
        print("\x1b[0;30;41m"+"Computer Better luck next time"+"\x1b[0m")
    elif (y > x):
        print("\x1b[6;30;42m"+"Computer is the winner of the game\n"+"\x1b[0m")
        print("\x1b[0;30;41m"+"Player Better luck next time"+"\x1b[0m")
    else:
        print("\x1b[0;30;43m"+"Its a Draw"+"\x1b[0m")

    print("\n")
    print("Player selections were")
    print(playerSelections)
    print("\n")
    print("Computer selections were")
    print(computerSelections)
    print("\n")
    playerSelections.clear()
    computerSelections.clear()
    x = 0
    y = 0
    z = 0

    # Asking user to play again
    mf.playAgain()
