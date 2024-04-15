
import random


def OutputDisplay(matrix):
    for i in matrix:
        print(i)


def ReturnMatrixWithValue(matrix, num, val):
    row = 0
    col = 0
    if num == 1:
        row = 0
        col = 0
    elif num == 2:
        row = 0
        col = 1
    elif num == 3:
        row = 0
        col = 2
    elif num == 4:
        row = 1
        col = 0
    elif num == 5:
        row = 1
        col = 1
    elif num == 6:
        row = 1
        col = 2
    elif num == 7:
        row = 2
        col = 0
    elif num == 8:
        row = 2
        col = 1
    elif num == 9:
        row = 2
        col = 2
    matrix[row][col] = val
    return matrix


def matrixCheck(matrix):
    winCheck = False
    if matrix[0][0] == matrix[0][1] == matrix[0][2] == "x" or matrix[1][0] == matrix[1][1] == matrix[1][2] == "x" or matrix[2][0] == matrix[2][1] == matrix[2][2] == "x" or matrix[0][0] == matrix[1][0] == matrix[2][0] == "x" or matrix[0][1] == matrix[1][1] == matrix[2][1] == "x" or matrix[0][2] == matrix[1][2] == matrix[2][2] == "x" or matrix[0][0] == matrix[1][1] == matrix[2][2] == "x" or matrix[2][0] == matrix[1][1] == matrix[0][2] == "x":
        winCheck = True
        value = "0"
    elif matrix[0][0] == matrix[0][1] == matrix[0][2] == "o" or matrix[1][0] == matrix[1][1] == matrix[1][2] == "o" or matrix[2][0] == matrix[2][1] == matrix[2][2] == "o" or matrix[0][0] == matrix[1][0] == matrix[2][0] == "o" or matrix[0][1] == matrix[1][1] == matrix[2][1] == "o" or matrix[0][2] == matrix[1][2] == matrix[2][2] == "o" or matrix[0][0] == matrix[1][1] == matrix[2][2] == "o" or matrix[2][0] == matrix[1][1] == matrix[0][2] == "o":
        winCheck = True
        #print("Player 1 Wins the Game")
        value = "x"
    return winCheck, value


matrix = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
refmatrix = [[1, 2, 3], [
    4, 5, 6], [7, 8, 9]]
checkList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
OutputDisplay(matrix)
print("\n")
OutputDisplay(refmatrix)

while True:

    if matrixCheck(matrix):
        print("Game ended")
        break
    elif not(matrixCheck) and not(checkList):
        print("Game is a Draw")
        print("Game ended")
        break

    while True:
        val = input(
            "\nPlayer 1 - Enter value between 1 to 9 which is not selected\n")
        if int(val) not in checkList:
            print("Incorrect value selected")
        else:
            print("Reference  matrix\n")
            OutputDisplay(refmatrix)
            print("\n")
            OutputDisplay((ReturnMatrixWithValue(matrix, int(val), "o")))
            checkList.remove(int(val))
            break

    while True:
        val = input(
            "\nPlayer 2 - Enter value between 1 to 9 which is not selected\n")
        if int(val) not in checkList:
            print("Incorrect value selected")
        else:
            print("Reference  matrix\n")
            OutputDisplay(refmatrix)
            print("\n")
            OutputDisplay((ReturnMatrixWithValue(matrix, int(val), "x")))
            checkList.remove(int(val))
            break
