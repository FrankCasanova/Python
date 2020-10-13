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
board[6][5] = True
board[6][4] = True
board[7][3] = True
board[7][2] = True


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
pulses = 20

for t in range(pulses):
    # prepare a new board
    newBoard = np.zeros([raws, colums], dtype=bool)

    # refresh the board
    for y in range(raws):
        for x in range(colums):
            # calculating the number of neighbors of the cell we're visiting
            n = 0
            if y > 0 and x > 0 and board[y-1][x-1]:
                n += 1
            if x > 0 and board[y][x-1]:
                n += 1
            if y < raws-1 and x > 0 and board[y+1][x-1]:
                n += 1
            if y > 0 and board[y-1][x]:
                n += 1
            if y < colums-1 and board[y+1][x]:
                n += 1
            if y > 0 and x < colums-1 and board[y-1][x+1]:
                n += 1
            if x < colums-1 and board[y][x+1]:
                n += 1
            if y < raws-1 and x < colums-1 and board[y+1][x+1]:
                n += 1

            # apply the rules
            if board[y][x] and (n == 2 or n == 3):  # survive
                newBoard[y][x] = True
            elif not board[y][x] and n == 3:  # born
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
