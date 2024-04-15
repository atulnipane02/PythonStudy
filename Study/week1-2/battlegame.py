# Defining the variable for characters to play game
wizard = "Wizard"
elf = "Elf"
human = "Human"
# Defining the varibale for health for characters
wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300
# Defining the varibale for damage for characters
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50
print("\nWelcome to the Battlegame\n")
while True:
    userChoice = input(
        "\n1)  Wizard\n2)  Elf\n3)  Human\nChoose your character:\n")
    if userChoice == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif userChoice == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif userChoice == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print(
            "\n Unknown character. Please select 1 for Wizrd, 2 for Elf and 3 for Human\n")


print("You have chosen character: "+character)
print("Health: "+str(my_hp))
print("Damage: "+str(my_damage)+"\n")

# Printing the battle result between selected character and dragon
while True:
    dragon_hp = dragon_hp - my_damage
    print("The "+character+" damaged the dragon")
    print("The Dragon's hitpoints are now: "+str(dragon_hp)+"\n")
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp = my_hp - dragon_damage
    print("The Dragon stikes back at "+character)
    print("The "+character+"'s hitpoints are now: "+str(my_hp)+"\n")
    if my_hp <= 0:
        print("The "+character+" has lost the battle")
        break
