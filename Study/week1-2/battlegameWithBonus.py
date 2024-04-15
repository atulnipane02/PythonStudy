#  Bonus Task1 - Completed
#  Bonus Task2 - Completed
#  Bonus Task3 - Completed
#  Bonus Task4 - Completed
#  Bonus Task5 - Completed

# Defining the variable for characters to play game
wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"
# Defining the varibale for health for characters
wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 175
# Defining the varibale for damage for characters
wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 125
print("\nWelcome to the Battlegame\n")
while True:
    # Defining Dragon attributes
    dragon_damage = 50
    dragon_hp = 300
    while True:
        userChoice = input(
            "\n1)  Wizard\n2)  Elf\n3)  Human\n4)  Orc\n5)  Exit\nChoose your option for character or to exit the game:\n")
        # To remove the before and after spaces in the user supplied string
        userChoice = userChoice.strip()
        if userChoice == "1" or userChoice.lower() == wizard.lower():
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif userChoice == "2" or userChoice.lower() == elf.lower():
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif userChoice == "3" or userChoice.lower() == human.lower():
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif userChoice == "4" or userChoice.lower() == orc.lower():
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        elif userChoice == "5" or userChoice.lower() == "exit":
            print("Exiting the Program")
            quit()
        else:
            print(
                "\n Unknown character. Please select 1 for Wizrd, 2 for Elf, 3 for Human, 4 for Orc and 5 for Exit. Also you can enter chanaracter name (Case Insensitive)\n")

    # Printing the character information for the selected character
    print("You have chosen character: "+character)
    print("Health: "+str(my_hp))
    print("Damage: "+str(my_damage)+"\n")

    # Printing the battle result between selected character and dragon
    while True:
        dragon_hp = dragon_hp - my_damage
        print("The "+character+" damaged the dragon")
        if dragon_hp < 0:
            print("The Dragon's hitpoints are now: 0\n")
        else:
            print("The Dragon's hitpoints are now: "+str(dragon_hp)+"\n")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break
        my_hp = my_hp - dragon_damage
        print("The Dragon stikes back at "+character)
        if my_hp <= 0:
            print("The "+character+"'s hitpoints are now: 0\n")
            print("The "+character+" has lost the battle")
            break
        else:
            print("The "+character+"'s hitpoints are now: "+str(my_hp)+"\n")

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
