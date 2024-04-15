def checkCharacter(password):
    special = "!@#$%^&*"
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    check1 = check2 = check3 = False
    for value in special:
        if value in password:
            check1 = True
            break
    for value in alpha:
        if value in password:
            check2 = True
            break
    for value in alpha.lower():
        if value in password:
            check3 = True
            break
    if check1 and check2 and check3:
        return True
    else:
        return False


password = "P@s"


print(checkCharacter(password))
