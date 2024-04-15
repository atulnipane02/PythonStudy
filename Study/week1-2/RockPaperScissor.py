x = 0
y = 0
z = 0

player1Selections = []
player2Selections = []

while True:
    print("\x1b[0;30;43m" +
          "\n Welcome to the Game of ROCK-PAPER-SSCISSOR \n"+"\x1b[0m")

    print("\x1b[0;30;46m"+"Following are the rules of the game:\n"+"1. Game will be consist of 3 rounds\n"+"2. For each round Player 1 will select 1 option out of Rock/Paper/Scissor and the Player 2 will do the same\n" +
          "3. Each round there can 3 outputs Player 1 wins/ Player 2 wins/ Daw\n"+"4. Winner will be declared at the end of the game depending upon the number of rounds won\n"+"5. Also game will end if first two rounds are won by same player"+"\x1b[0m")

    while x+y+z < 3:

        while True:
            val1 = input(
                "\n Player 1 please select your option. Enter the number for the option.\n 1. ROCK \n 2. PAPER \n 3. SCISSOR \n\n")
            val1 = val1.strip()
            if val1 == "1" or val1.lower() == "rock":
                player1Option = "ROCK"
                break
            elif val1 == "2" or val1.lower() == "paper":
                player1Option = "PAPER"
                break
            elif val1 == "3" or val1.lower() == "scissor":
                player1Option = "SCISSOR"
                break
            else:
                print("\n Please select correct option \n")
        player1Selections.append(player1Option.upper())

        while True:
            val2 = input(
                "\n Player 2 please select your option. Enter the number for the option.\n 1. ROCK \n 2. PAPER \n 3. SCISSOR \n\n")
            val2 = val2.strip()
            if val2 == "1" or val2.lower() == "rock":
                player2Option = "ROCK"
                break
            elif val2 == "2" or val2.lower() == "paper":
                player2Option = "PAPER"
                break
            elif val2 == "3" or val2.lower() == "scissor":
                player2Option = "SCISSOR"
                break
            else:
                print("\n Please select correct option \n")

        player2Selections.append(player2Option.upper())

        if (player1Option == "ROCK" and player2Option == "SCISSOR") or (player1Option == "SCISSOR" and player2Option == "PAPER") or (player1Option == "PAPER" and player2Option == "ROCK"):
            x = x+1
            if x > 1:
                break
        elif (player2Option == "ROCK" and player1Option == "SCISSOR") or (player2Option == "SCISSOR" and player1Option == "PAPER") or (player2Option == "PAPER" and player1Option == "ROCK"):
            y = y+1
            if y > 1:
                break
        else:
            z = z+1

    print("\n")
    if (x > y):
        print("\x1b[6;30;42m"+"Player 1 is the winner\n"+"\x1b[0m")
        print("\x1b[0;30;41m"+"Player 2 Better luck next time"+"\x1b[0m")
    elif (y > x):
        print("\x1b[6;30;42m"+"Player 2 is the winner\n"+"\x1b[0m")
        print("\x1b[0;30;41m"+"Player 1 Better luck next time"+"\x1b[0m")
    else:
        print("\x1b[0;30;43m"+"Its a Draw"+"\x1b[0m")

    print("\n")
    print("Player 1 selections are")
    print(player1Selections)
    print("\n")
    print("Player 2 selections are")
    print(player2Selections)
    print("\n")
    player1Selections.clear()
    player2Selections.clear()
    x = 0
    y = 0
    z = 0

    # Asking user to play again
    while True:
        playagain = input(
            "Do you want to play again?\n1. Yes\t2. No\nYou can also put the name (Case Insensitive)")
        # To remove the before and after spaces in the user supplied string
        playagain = playagain.strip()
        if playagain == "1" or playagain.lower() == "yes":
            break
        elif playagain == "2" or playagain.lower() == "no":
            quit()
        else:
            print("\nIncorrect option selected. Please select right option")
