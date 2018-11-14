import lib
import random

def checkAvaibility(field, num):
    op = []
    for n in range(len(field)):
        for i in range(len(field[n])):
            if(num == field[n][i]):
                op += [[n, i]]
    ans = []
    for n in op:
        for i in op:
            if(n != i and (n[0] == i[0]-1 or n[0] == i[0]+1 or n[0] == i[0]) and (n[1] == i[1] or n[1] == i[1]-1 or n[1] == i[1]+1)):
                ans += [[n, i]]
                op.remove(i)
    return ans

def turn(field):
    col = random.randint(0,2)
    row = random.randint(0,2)
    while lib.check(field, col, row) > 0:
        col = random.randint(0,2)
        row = random.randint(0,2)
    return col, row
