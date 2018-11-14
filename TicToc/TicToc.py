import lib

currentPlayer = 0
player = lib.initialization()
winner = -1
field = [[0,0,0],[0,0,0],[0,0,0]]

lib.displayField(field)

while winner < 0:
    if(currentPlayer == 0):
        print("This is X's turn")
    else:
        print("This is O's turn")
    field = lib.turn(field, player, currentPlayer)
    lib.displayField(field)
    
    if(lib.victory(field, currentPlayer)):
        winner = currentPlayer + 1
    elif(lib.draw(field)):
        winner = 3

    if(currentPlayer == 0):
        currentPlayer = 1
    else:
        currentPlayer = 0


if(winner > 2):
    print("Draw!")
else:
    print("winner is player number", winner);

