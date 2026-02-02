import time, copy, os

WIDTH = 6
HEIGHT = 6
SIZE = 6
boarda = []

# Generowanie planszy
for x in range(WIDTH):
    for y in range(HEIGHT):
        boarda.append(0)

boarda = [boarda[i:i+SIZE] for i in range(0, len(boarda), SIZE)]

boarda[2][3] = 1
boarda[3][4] = 1
boarda[4][4] = 1
boarda[4][3] = 1
boarda[4][2] = 1

while True:
    board = copy.deepcopy(boarda)
    # rysowanie planszy
    for x in range(WIDTH):
        for y in range(HEIGHT):
                print(str(boarda[x][y]) + ' ',end="")
        print()


    # sprawdzanie pól sąsiednich

    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x-1)%WIDTH
            right = (x+1)%WIDTH
            up = (y-1)%HEIGHT
            down = (y+1)%HEIGHT

            numOfNeighbours = 0
            if board[left][up] == 1:
                numOfNeighbours += 1
            if board[left][y] == 1:
                numOfNeighbours += 1
            if board[left][down] == 1:
                numOfNeighbours += 1
            if board[right][up] == 1:
                numOfNeighbours += 1
            if board[right][y] == 1:
                numOfNeighbours += 1
            if board[right][down] == 1:
                numOfNeighbours += 1
            if board[x][up] == 1:
                numOfNeighbours += 1
            if board[x][down] == 1:
                numOfNeighbours += 1

            if (numOfNeighbours == 3 or numOfNeighbours == 2) and board[x][y] == 1:
                boarda[x][y] = 1
            elif numOfNeighbours == 3 and board[x][y] == 0:
                boarda[x][y] = 1
            else:
                boarda[x][y] = 0
    time.sleep(1)
