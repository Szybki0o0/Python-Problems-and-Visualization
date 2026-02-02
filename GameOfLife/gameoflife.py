import time, copy, random

WIDTH = 20
HEIGHT = 20
SIZE = 20
board = []

# Generowanie planszy
for x in range(WIDTH):
    for y in range(HEIGHT):
        board.append(random.randint(0,1))

board = [board[i:i+SIZE] for i in range(0, len(board), SIZE)]

# Pętla główna
while True:
    currentBoard = copy.deepcopy(board)
    # rysowanie planszy
    for x in range(WIDTH):
        for y in range(HEIGHT):
                print(str(board[x][y]) + ' ',end="")
        print()

    # sprawdzanie pól sąsiednich
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x-1)%WIDTH
            right = (x+1)%WIDTH
            up = (y-1)%HEIGHT
            down = (y+1)%HEIGHT

            numOfNeighbours = 0
            if currentBoard[left][up] == 1:
                numOfNeighbours += 1
            if currentBoard[left][y] == 1:
                numOfNeighbours += 1
            if currentBoard[left][down] == 1:
                numOfNeighbours += 1
            if currentBoard[right][up] == 1:
                numOfNeighbours += 1
            if currentBoard[right][y] == 1:
                numOfNeighbours += 1
            if currentBoard[right][down] == 1:
                numOfNeighbours += 1
            if currentBoard[x][up] == 1:
                numOfNeighbours += 1
            if currentBoard[x][down] == 1:
                numOfNeighbours += 1

            # logika gry
            if (numOfNeighbours == 3 or numOfNeighbours == 2) and currentBoard[x][y] == 1:
                board[x][y] = 1
            elif numOfNeighbours == 3 and currentBoard[x][y] == 0:
                board[x][y] = 1
            else:
                board[x][y] = 0
    time.sleep(1)
