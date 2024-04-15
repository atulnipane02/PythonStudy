
import random as r
import csv

while True:
    fileName = input(
        "Input name of the file where you want to store the results: ")
    if fileName.isalnum() and len(fileName) > 0:
        fileName = fileName.strip()+".csv"
        break
    else:
        print("Filename should be alphanumeric only. Also length should be greater than 0")

outfile = open(fileName, 'w')
outfile_header = "Player Name,Player Cards,Player Count,Balance,Bet Amount,Loss,Gain,BJStatus,Dealer Cards,Dealer Count\n"
outfile.write(outfile_header)
playerList = []
dealerCardList = []


# Displaying cards for dealer and all players
def displayGameData(dealerCardList, playerList):
    print("\x1b[0;30;46m", "Dealer Cards", dealerCardList,
          "Total - ", totalCount(dealerCardList), "\x1b[0m", end=" ")
    for player in playerList:
        if len(player.playerCardList) > 0:
            if isinstance(player.playerCardList[0], list):
                for i in range(0, 2, 1):
                    print("\x1b[0;30;46m", player.name, "Round-", i+1, player.playerCardList[i],
                          "Total -", totalCount(player.playerCardList[i]), "\x1b[0m", end=" ")
            else:
                print("\x1b[0;30;46m", player.name, player.playerCardList,
                      "Total -", totalCount(player.playerCardList), "\x1b[0m", end=" ")
        else:
            print("\x1b[0;30;46m", player.name, player.playerCardList,
                  "Total -", totalCount(player.playerCardList), "\x1b[0m", end=" ")


# Printing the text in color provided by the user
def printingTextWithcolor(text, color):
    if color.lower() == "red":
        print("\x1b[0;30;41m"+text+"\x1b[0m")
    elif color.lower() == "green":
        print("\x1b[6;30;42m"+text+"\x1b[0m")
    elif color.lower() == "yellow":
        print("\x1b[0;30;43m"+text+"\x1b[0m")
    elif color.lower() == "blue":
        print("\x1b[0;30;46m"+text+"\x1b[0m")
    elif color.lower() == "purple":
        print("\x1b[0;30;45m"+text+"\x1b[0m")


# Drawing card from the deck
def CardDraw(cardList, deck):
    card = r.choice(deck.deckList)
    deck.deckList.remove(card)
    cardList.append(card)


# Play again module
def playAgain():
    while True:
        playagain = input(
            "Do you want to play again?\n1. Yes\t2. No\nYou can also put the name (Case Insensitive): ")
        # To remove the before and after spaces in the user supplied string
        playagain = playagain.strip()
        if playagain == "1" or playagain.lower() == "yes":
            break
        elif playagain == "2" or playagain.lower() == "no":
            quit()
        else:
            text = "\nIncorrect option selected. Please select right option: "
            printingTextWithcolor(text, "red")


# Getting sum of the cards
def totalCount(cardList):
    sum = 0
    count = 0
    for val in cardList:
        value = 0
        if val[0] == "T" or val[0] == "J" or val[0] == "Q" or val[0] == "K":
            value = 10
        elif val[0] == "A":
            count = count + 1
        else:
            value = int(val[0])
        sum = value + sum
    # Handling the Ace situation
    if sum <= 10 and count > 1 and sum+10+count <= 21:
        sum = sum + count + 10
    elif sum <= 10 and count > 1 and sum+10+count > 21:
        sum = sum + count
    elif sum > 10 and count > 1:
        sum = sum + count
    elif sum <= 10 and count == 1:
        sum = sum + 11
    elif sum > 10 and count == 1:
        sum = sum + count
    return sum


# Function to perform to bet amount for each player
def betFunction():
    for player in playerList:
        while True:
            print("\n")
            betAmount = input(
                "\x1b[3;30;47m"+player.name+" enter amount to bet (Amount should be whole number and Minimum bet amount is $5):"+"\x1b[0m")
            betAmount = betAmount.strip()
            if betAmount.isnumeric() and float(betAmount) <= player.balance and int(betAmount) >= 5:
                player.changeBetAmount(float(betAmount))
                player.reduceBalance(float(betAmount))
                break
            else:
                print(
                    "Either incorrect amount is entered or amount entered is greater than amount you have. You have "+str(player.balance)+" in your wallet.")


# Function to perform split and play for each player
def playersDefinition():
    while True:
        noOfPlayer = input("Enter number of player playing: ")
        noOfPlayer = noOfPlayer.strip()
        deck.deckCreation(int(noOfPlayer))
        if noOfPlayer.isdigit() and int(noOfPlayer) > 0:
            for i in range(0, int(noOfPlayer), 1):
                while True:
                    print("\n")
                    print("Player-", i+1, "turn")
                    playerName = input("Enter the name: ")
                    playerName = playerName.strip()
                    if playerName.isalnum():
                        player = Player(playerName)
                        playerList.append(player)
                        break
                    else:
                        print("Enter only alphanumeric values in name")
            break
        else:
            print("Please enter only numbers greater than 0")


def playGame():
    CardDraw(dealerCardList, deck)
    for player in playerList:
        print("\n")
        CardDraw(player.playerCardList, deck)
        CardDraw(player.playerCardList, deck)
        player.bjListStatus[player.name] = []
        if player.playerCardList[0][0] == player.playerCardList[1][0]:
            while True:
                print("\n")
                displayGameData(dealerCardList, playerList)
                print("\n")
                splitInput = input(
                    "\x1b[3;30;47m"+"\n"+player.name+"-Do you want to split?\t1.Yes\t2.No : "+"\x1b[0m")
                if splitInput == "1":
                    if player.balance >= player.betAmount:
                        card1 = player.playerCardList[0]
                        card2 = player.playerCardList[1]
                        player.playerCardList.clear()
                        player.playerCardList = [[], []]
                        player.playerCardList[0].append(card1)
                        player.playerCardList[1].append(card2)
                        player.bjListStatus[player.name] = [[], []]
                        player.reduceBalance(player.betAmount)
                        break
                    else:
                        print(
                            player.name, " does not have enough money to split. Normal game will continue.")
                        break
                elif splitInput == "2":
                    break
                else:
                    printingTextWithcolor(
                        "Incorrect Option selected.\n", "red")
    displayGameData(dealerCardList, playerList)
    print("\n")
    for player in playerList:
        if isinstance(player.playerCardList[0], list):
            for i in range(0, 2, 1):
                print(player.name+" round-", i+1, " begins.\n")
                while True:
                    if totalCount(player.playerCardList[i]) > 21:
                        displayGameData(dealerCardList, playerList)
                        print("\n")
                        text = player.name+"- busted in round "+str(i+1)
                        print("\n")
                        printingTextWithcolor(text, "red")
                        player.bjListStatus[player.name][i].append("Busted")
                        line = "{},{},{},{},{},{},{},{},{},{}\n".format(
                            player.name, player.playerCardList[i], totalCount(player.playerCardList[i]), player.balance, player.betAmount, player.betAmount, "NA", player.bjListStatus[player.name][i], dealerCardList, totalCount(dealerCardList))
                        outfile.write(line)
                        break
                    elif totalCount(player.playerCardList[i]) == 21:
                        displayGameData(dealerCardList, playerList)
                        print("\n")
                        text = player.name+" hit Black Jack for round " + \
                            str(i+1)+"\n"
                        printingTextWithcolor(text, "green")
                        player.bjListStatus[player.name][i].append(
                            "BlackJack")
                        line = "{},{},{},{},{},{},{},{},{},{}\n".format(
                            player.name, player.playerCardList[i], totalCount(player.playerCardList[i]), player.balance, player.betAmount, "NA", 3 * player.betAmount, player.bjListStatus[player.name][i], dealerCardList, totalCount(dealerCardList))
                        outfile.write(line)
                        break
                    playInput = input("\n"+"\x1b[3;30;47m" +
                                      player.name+"-Do you want to hit or Stay?\t1.Hit\t2.Stay: "+"\x1b[0m")
                    if playInput == "1":
                        CardDraw(player.playerCardList[i], deck)
                        displayGameData(dealerCardList, playerList)
                        print("\n")
                        print("\x1b[0;30;43m"+"Player Cards:",
                              player.name, player.playerCardList[i], " Total: ", totalCount(player.playerCardList[i]), "\x1b[0m")
                    elif playInput == "2":
                        player.bjListStatus[player.name][i].append(
                            "Normal")
                        break
                    else:
                        printingTextWithcolor(
                            "Incorrect option is selected\n", "red")
        else:
            while True:
                if totalCount(player.playerCardList) > 21:
                    displayGameData(dealerCardList, playerList)
                    text = player.name+" is busted"
                    print("\n")
                    printingTextWithcolor(text, "red")
                    print("\n")
                    player.bjListStatus[player.name].append("Busted")
                    line = "{},{},{},{},{},{},{},{},{},{}\n".format(
                        player.name, player.playerCardList, totalCount(player.playerCardList), player.balance, player.betAmount, player.betAmount, "NA", player.bjListStatus[player.name], dealerCardList, totalCount(dealerCardList))
                    outfile.write(line)
                    break
                elif totalCount(player.playerCardList) == 21:
                    displayGameData(dealerCardList, playerList)
                    text = player.name+" hit Black Jack"
                    print("\n")
                    printingTextWithcolor(text, "green")
                    print("\n")
                    player.bjListStatus[player.name].append("BlackJack")
                    line = "{},{},{},{},{},{},{},{},{},{}\n".format(
                        player.name, player.playerCardList, totalCount(player.playerCardList), player.balance, player.betAmount, "NA", 3 * player.betAmount, player.bjListStatus[player.name], dealerCardList, totalCount(dealerCardList))
                    outfile.write(line)
                    break
                playInput = input("\n"+"\x1b[3;30;47m" +
                                  player.name+"-Do you want to hit or Stay?\t1.Hit\t2.Stay: "+"\x1b[0m")
                if playInput == "1":
                    CardDraw(player.playerCardList, deck)
                    displayGameData(dealerCardList, playerList)
                    print("\n")
                    print("\x1b[0;30;43m"+"Player Cards:",
                          player.name, player.playerCardList, " Total: ", totalCount(player.playerCardList), "\x1b[0m")
                elif playInput == "2":
                    player.bjListStatus[player.name].append(
                        "Normal")
                    break
                else:
                    printingTextWithcolor(
                        "Incorrect option is selected", "red")


# Function to peform dealer steps and show results
def dealerPlaysAndResult():
    while True:
        if totalCount(dealerCardList) > 21:
            displayGameData(dealerCardList, playerList)
            print("\n")
            print("\x1b[0;30;43m"+"Dealer Cards:",
                  dealerCardList, "\x1b[0m")
            break
        elif totalCount(dealerCardList) == 21:
            displayGameData(dealerCardList, playerList)
            print("\n")
            print("\x1b[0;30;43m"+"Dealer Cards:",
                  dealerCardList, "\x1b[0m")
            print("\n")
            break
        playInput = input(
            "\n"+"\x1b[3;30;47m"+"Do you want to hit or Stay?\t1.Hit\t2.Stay: "+"\x1b[0m")
        if playInput == "1":
            CardDraw(dealerCardList, deck)
            displayGameData(dealerCardList, playerList)
            print("\n")
            print("\x1b[0;30;43m"+"Dealer Cards:",
                  dealerCardList, " Total: ", totalCount(dealerCardList), "\x1b[0m")
        elif playInput == "2":
            break
        else:
            printingTextWithcolor("Incorrect option is selected", "red")

        print("\n")
    print("-----------------------------------GAME RESULTS-------------------------------------------------")
    for player in playerList:
        if isinstance(player.playerCardList[0], list):
            for i in range(0, 2, 1):
                if player.bjListStatus[player.name][i][0] != "Busted" and player.bjListStatus[player.name][i][0] != "BlackJack" and totalCount(dealerCardList) <= 21:
                    if totalCount(dealerCardList) > totalCount(player.playerCardList[i]):
                        text = player.name+" lost to dealer in round" + \
                            str(i+1) + \
                            ". Amount Lost" + \
                            str(player.betAmount) + \
                            ". Amount Remaining"+str(player.balance)
                        printingTextWithcolor(text, "red")
                        line = "{},{},{},{},{},{},{},{},{},{}\n".format(
                            player.name, player.playerCardList[i], totalCount(player.playerCardList[i]), player.balance, player.betAmount, "NA", player.betAmount, player.bjListStatus[player.name][i], dealerCardList, totalCount(dealerCardList))
                        outfile.write(line)
                    elif totalCount(dealerCardList) < totalCount(player.playerCardList[i]):
                        player.addBalance(2 * player.betAmount)
                        text = player.name + \
                            " won against the dealer in round" + \
                            str(
                                i+1)+". Amount Won: $"+str(player.betAmount)+" Amount Remaining: $"+str(player.balance)
                        printingTextWithcolor(text, "green")
                        line = "{},{},{},{},{},{},{},{},{},{}\n".format(
                            player.name, player.playerCardList[i], totalCount(player.playerCardList[i]), player.balance, player.betAmount, "NA", player.betAmount, player.bjListStatus[player.name][i], dealerCardList, totalCount(dealerCardList))
                        outfile.write(line)
                    else:
                        player.addBalance(player.betAmount)
                        text = player.name + \
                            " draws against the dealer in round-" + \
                            str(i +
                                1)+" Amount Remaining: $"+str(player.balance)
                        printingTextWithcolor(text, "yellow")
                        line = "{},{},{},{},{},{},{},{},{},{}\n".format(
                            player.name, player.playerCardList[i], totalCount(player.playerCardList[i]), player.balance, player.betAmount, "NA", "NA", player.bjListStatus[player.name][i], dealerCardList, totalCount(dealerCardList))
                        outfile.write(line)
                elif player.bjListStatus[player.name][i][0] == "BlackJack":
                    player.addBalance(4 * player.betAmount)
                    text = player.name+" already hit the Black Jack." + \
                        player.name+" beats the dealer in round-" + \
                        str(i+1)+". Amount Won: $"+str(
                            3 * player.betAmount)+" Amount Remaining: $" + str(player.balance)
                    printingTextWithcolor(text, "green")
                elif player.bjListStatus[player.name][i][0] == "Busted":
                    text = player.name+" already been Busted." + \
                        player.name+" lost to the dealer in round-" + \
                        str(
                            i+1)+". Amount Lost: $"+str(player.betAmount) + ". Amount Remaining: $"+str(player.balance)
                    printingTextWithcolor(text, "red")
                else:
                    player.addBalance(2*player.betAmount)
                    text = "Dealer has been busted."+player.name + \
                        " has won against the dealer in the round-" + \
                        str(i+1) + \
                        ". Amount Won: $" + \
                        str(player.betAmount) + \
                        " Amount Remaining: $"+str(player.balance)
                    printingTextWithcolor(text, "green")
                    line = "{},{},{},{},{},{},{},{},{},{}\n".format(
                        player.name, player.playerCardList[i], totalCount(player.playerCardList[i]), player.balance, player.betAmount, "NA", player.betAmount, player.bjListStatus[player.name][i], dealerCardList, totalCount(dealerCardList))
                    outfile.write(line)
        else:
            if player.bjListStatus[player.name][0] != "Busted" and player.bjListStatus[player.name][0] != "BlackJack" and totalCount(dealerCardList) <= 21:
                if totalCount(dealerCardList) > totalCount(player.playerCardList):
                    text = player.name + " lost to dealer." + ". Amount Lost: $" + \
                        str(player.betAmount) + \
                        ". Amount Remaining: $"+str(player.balance)
                    printingTextWithcolor(text, "red")
                    line = "{},{},{},{},{},{},{},{},{},{}\n".format(
                        player.name, player.playerCardList, totalCount(player.playerCardList), player.balance, player.betAmount, player.betAmount, "NA", player.bjListStatus[player.name], dealerCardList, totalCount(dealerCardList))
                    outfile.write(line)
                elif totalCount(dealerCardList) < totalCount(player.playerCardList):
                    player.addBalance(2 * player.betAmount)
                    text = player.name + " won against the dealer." + \
                        ". Amount Won: $" + \
                        str(player.betAmount) + \
                        " Amount Remaining: $"+str(player.balance)
                    printingTextWithcolor(text, "green")
                    line = "{},{},{},{},{},{},{},{},{},{}\n".format(
                        player.name, player.playerCardList, totalCount(player.playerCardList), player.balance, player.betAmount, "NA", player.betAmount, player.bjListStatus[player.name], dealerCardList, totalCount(dealerCardList))
                    outfile.write(line)
                else:
                    player.addBalance(player.betAmount)
                    text = player.name+" draws against the dealer." + \
                        " Amount Remaining: $"+str(player.balance)
                    printingTextWithcolor(text, "yellow")
                    line = "{},{},{},{},{},{},{},{},{},{}\n".format(
                        player.name, player.playerCardList, totalCount(player.playerCardList), player.balance, player.betAmount, "NA", "NA", player.bjListStatus[player.name], dealerCardList, totalCount(dealerCardList))
                    outfile.write(line)
            elif player.bjListStatus[player.name][0] == "BlackJack":
                player.addBalance(4 * player.betAmount)
                text = player.name+" already hit the Black Jack." + player.name+" beats the dealer" + ". Amount Won: $" + \
                    str(3 * player.betAmount) + \
                    " Amount Remaining: $" + str(player.balance)
                printingTextWithcolor(text, "green")
            elif player.bjListStatus[player.name][0] == "Busted":
                text = player.name + " already been Busted." + player.name + " lost to the dealer"+". Amount Lost: $" + \
                    str(player.betAmount) + \
                    ". Amount Remaining: $"+str(player.balance)
                printingTextWithcolor(text, "red")
            else:
                player.addBalance(2 * player.betAmount)
                text = "Dealer has been busted."+player.name + " has won against the dealer"+". Amount Won: $" + \
                    str(player.betAmount) + \
                    " Amount Remaining: $"+str(player.balance)
                printingTextWithcolor(text, "green")
                line = "{},{},{},{},{},{},{},{},{},{}\n".format(
                    player.name, player.playerCardList, totalCount(player.playerCardList), player.balance, player.betAmount, "NA", player.betAmount, player.bjListStatus[player.name], dealerCardList, totalCount(dealerCardList))
                outfile.write(line)
    print("------------------------------------------------------------------------------------------------")
    print("\n")


class Player:
    def __init__(self, name):
        self.name = name
        self.playerCardList = []
        self.betAmount = 0
        self.balance = 50.0
        self.bjListStatus = {}

    def addCard(self, card):
        self.playerCardList.append(card)

    def addBalance(self, amount):
        self.balance += amount

    def reduceBalance(self, amount):
        self.balance -= amount

    def showPlayerCards(self):
        for card in self.playerCardList:
            print(card)

    def changeBetAmount(self, betAmount):
        self.betAmount = betAmount


class Deck:
    def __init__(self):
        self.deckList = ['AS', 'AD', 'AH', 'AF', '2S', '2D', '2H', '2F', '3S', '3D', '3H', '3F', '4S', '4D', '4H', '4F', '5S', '5D', '5H', '5F', '6S', '6D', '6H', '6F', '7S',
                         '7D', '7H', '7F', '8S', '8D', '8H', '8F', '9S', '9D', '9H', '9F', 'TS', 'TD', 'TH', 'TF', 'JS', 'JD', 'JH', 'JF', 'QS', 'QD', 'QH', 'QF', 'KS', 'KD', 'KH', 'KF']

    def deckCreation(self, num):
        self.deckList = num * self.deckList


welcomeText = "\n Welcome to the Game of BLACK JACK \n"
rules = "Following are the rules of the game:\n"+"1. User will be asked how many players ae playing the game\n"+"2. Upon selection every player has to put a bet.(By default every player is assigned with $50) \n"+"3. After putting bet all player will be assigned 2 cards to players and 1 to dealer (All player can see dealer and other player cards)\n" + "4. Every player will get a turn to get more cards or can stay\n" + \
    "5. Player can split the turn if they get same cards in first attempt\n" + \
    "6. After all players done playing dealer will play\n" + \
    "7. After dealers turn result will be displayed (If player hits Black Jack (Exact 21 count) they will get 3 times the betted amount. If player is busted (count>21) they will loose betted amount. If player count is less than 21 but greater than count of dealer they will get double the betted amount)"

printingTextWithcolor(welcomeText, "yellow")
printingTextWithcolor(rules, "blue")
print("\n")
deck = Deck()
playersDefinition()
while True:
    betFunction()
    playGame()
    print("\n")
    print("\nDealers turn to Play:")
    dealerPlaysAndResult()
    for player in playerList:
        player.playerCardList.clear()
    dealerCardList.clear()
    playAgain()
