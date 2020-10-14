# Have the game of life program ask the user for the number of living neighbor
# cells needed for the different rules to fire and show how the board evolves with them

# original code update v2.

import numpy as np

# number of files and colums
raws = 10
colums = 10

# creating a matrix
board = np.zeros([raws, colums], dtype=bool)

# part of the matrix with living cells
board[2][2] = True
board[2][3] = True
board[3][4] = True
board[4][5] = True
board[5][5] = True
board[6][4] = True
board[7][3] = True
board[7][2] = True

nbToActivate = int(input('Number of neighbor cells need to live:\n\n'))

# representing board
print('Initial state:')
for y in range(raws):
    for x in range(colums):
        if board[y][x]:
            print('*', end='')
        else:
            print('.', end='')

    print()


# number of pulses
pulses = 10

for t in range(pulses):
    # prepare a new board
    newBoard = np.zeros([raws, colums], dtype=bool)

    # refresh the board
    for y in range(raws):
        for x in range(colums):
            # calculating the number of neighbors of the cell we're visiting
            n = 0
            if board[y][x]:
                n = -1
            else:
                n = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if y + i >= 0 and y + i < raws and x + y >= 0 and x + j < colums:
                        if board[y+i][x+j]:
                            n += 1

            # apply the rules
            if board[y][x] and (n == nbToActivate or n == nbToActivate):  # survive
                newBoard[y][x] = True
            elif not board[y][x] and n == nbToActivate:  # born
                newBoard[y][x] = True
            else:  # overpopulation
                newBoard[y][x] = False

    # refresh the board
    board = newBoard

    # represent the board
    print('pulses', t + 1)
    for y in range(raws):
        for x in range(colums):
            if board[y][x]:
                print('*', end='')
            else:
                print('.', end='')

        print()
