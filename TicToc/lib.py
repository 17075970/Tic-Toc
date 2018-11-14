import AI
import random

def initialization():
    a = 0
    while a < 1 or a > 2:
        a = int(input("Enter the number of players: "))
    if(a == 2):
        ans = [True, True]
    else:
        while(a != "Yes" and a != "No"):
            a = str(input("Does player go first? "))
        if(a == "Yes"):
            ans = [True, False]
        else:
            ans = [False, True]
    return ans

def displayField(field):
    a = "  0 1 2\n"
    for n in range(len(field)):
        a += str(n) + " "
        for i in range(len(field[n])):
            if(field[n][i] == 0):
                a += "- "
            elif(field[n][i] == 1):
                a += "X "
            else:
                a += "O "
        a += "\n"
    print(a)

def check(field, col, row):
    return field[row][col]

def turn(field, player, currentPlayer):
    end = False
    while not end:
        if(player[currentPlayer]):
            col = int(input("Enter the column: "))
            row = int(input("Enter the row: "))
            print("")
            if(col >= 0 and col <= 2 and row >= 0 and row <= 2):
                if(check(field, col, row) == 0):
                    end = True
                    field[row][col] = currentPlayer+1
            else:
                print("Out of range")
        else:
            col, row = AI.turn(field)
            field[row][col] = currentPlayer+1
            end = True
    return field

def draw(field):
    ans = 0
    for n in range(len(field)):
        for i in range(len(field[n])):
            if(field[n][i]>0):
                ans+=1
    if(ans == 9):
        ans = True
    else:
        ans = False
    return ans

def victory(field, currentPlayer):
    finish = False
    nPlayer = currentPlayer + 1
    if(nPlayer == field[1][1] and ((nPlayer == field[0][0] and nPlayer == field[2][2]) or (nPlayer == field[0][2] and nPlayer == field[2][0]))):
        finish = True
    else:
        for n in range(len(field)):
            if(nPlayer == field[n][0] and nPlayer == field[n][1] and nPlayer == field[n][2]):
                finish = True
            elif(nPlayer == field[0][n] and nPlayer == field[1][n] and nPlayer == field[2][n]):
                finish = True
    return finish
