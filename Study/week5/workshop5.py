# Task 1-3 Completed
# Bonus Task 1-4 Completed

import random as r


# Guessing number through user input. Also includes Bonus task 1 and Bonus task 3
def guess_random_number(tries, start, stop):
    num = r.randint(start, stop)
    userGuessList = []
    while tries > 0:
        print("Number of tries left", tries, "\n")
        while True:
            userGuess = input("Guess a number between " +
                              str(start)+" and "+str(stop)+":")
            if userGuess.isnumeric() and int(userGuess) in range(start, stop):
                userGuess = int(userGuess)
                if userGuess not in userGuessList:
                    userGuessList.append(userGuess)
                    break
                else:
                    print("Number selected already tried by the user")
            else:
                print(
                    "Entered value should contain only number within range", start, "and", stop)
        if num == userGuess:
            print("You guessed the correct number\n")
            return True
        elif num > userGuess:
            print("Guess higher!")
        elif num < userGuess:
            print("Guess lower!")
        tries -= 1
    print("You have failed to guess the number", num)


# Guess the number programmatically through linear search
def guess_random_num_linear(tries, start, stop):
    num = r.randint(start, stop)

    for val in range(start, stop, 1):
        if tries > 0:
            print("Number of tries left", tries, "\n")
            print("The program is guessing...", val)
            if val == num:
                print("The program has guessed the correct number\n", num)
                return True
            else:
                tries = tries-1
        else:
            print("The program has failed to guess the correct number.", num)
            return False


# Guess the number programmatically using binary search.
def guess_random_num_binary(tries, start, stop):
    num = r.randint(start, stop)
    lower_bound = start
    upper_bound = stop
    print("Random number to find:", num)
    while lower_bound <= upper_bound:
        if tries > 0:
            pivot = (lower_bound + upper_bound) // 2
            print(pivot)
            if pivot == num:
                print("Found it", num)
                return True
            elif pivot > num:
                print("Guessing higher!")
                upper_bound = pivot - 1
                tries = tries - 1
            else:
                print("Guessing lower!")
                lower_bound = pivot + 1
                tries = tries - 1
        else:
            print("Your program failed to find the number:", num)
            return False


# Bonus task 2
def selectMethod():
    userTries = input(
        "Enter the number of tries allowed to guess the number: ")
    rangeStart = input("Enter the start value of the Range: ")
    rangeStop = input("Enter the stop value of the Range:  ")
    userTries = int(userTries)
    rangeStart = int(rangeStart)
    rangeStop = int(rangeStop)
    while True:
        methodSelect = input(
            "Select which method you want to use to perform the search.\t1. User Input\t2. Linear Search\t3. Binary Search: ")
        if methodSelect == "1":
            guess_random_number(userTries, rangeStart, rangeStop)
            break
        elif methodSelect == "2":
            guess_random_num_linear(userTries, rangeStart, rangeStop)
            break
        elif methodSelect == "3":
            guess_random_num_binary(userTries, rangeStart, rangeStop)
            break
        else:
            print("Incorrect option selected")


# Bonus task 4
def gamble():
    playerBalance = 10
    while True:
        print("Your balance is $", playerBalance,
              "You need to  earrn more than $50 to win game.  If your balance goes to 0 or below you will lose")
        while True:
            playerBetAmount = input("Enter amount to bet: ")
            if playerBetAmount.isnumeric() and int(playerBetAmount) in range(1, 11):
                playerBetAmount = int(playerBetAmount)
                break
            else:
                print("Entered value need to be only number and between 1 and 10. Also check whether your value is lesser than the balance value", playerBalance)
        while True:
            winPrediction = input(
                "Will computer guess the correct numbe or not?\t1. Yes \t2. No (You can enter 1/y/yes/YES or 2/n/no/NO)")
            if winPrediction == "1" or winPrediction.lower() == "yes" or winPrediction.lower() == "y":
                winPrediction = "Yes"
                break
            elif winPrediction == "2" or winPrediction.lower() == "no" or winPrediction.lower() == "n":
                winPrediction = "No"
                break
            else:
                print("Enter correct value")

        check = guess_random_num_linear(5, 0, 10)

        if check == True and winPrediction == "Yes":
            playerBalance += playerBetAmount
        elif check == False and winPrediction == "No":
            playerBalance += playerBetAmount
        else:
            playerBalance -= playerBetAmount

        if playerBalance > 50:
            print("Player wins the game. Your balance is $", playerBalance)
            break
        elif playerBalance <= 0:
            print("Player lost the game. Your balance is $0")
            break


# gamble()
# selectMethod()
#guess_random_number(5, 0, 10)
#guess_random_num_linear(5, 0, 10)
#guess_random_num_binary(5, 0, 100)
