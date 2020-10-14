import numpy as np

# unidimensional board
raw = 10

board = np.zeros((raw), dtype=int)

board[4] = 1

# represent the board

print('initial state')
for i in range(raw):
    if board[i] == 1:
        print('*', end='')
    else:
        print('.', end='')


pulses = 10

for t in range(pulses):
    # new board
    newBoard = np.zeros((raw), dtype=bool)
    for i in range(raw):

    board = newBoard
    print('pulses', t + 1)
    for i in range(raw):
        if board[i] == 1:
            print('*', end='')
        else:
            print('.', end='')
