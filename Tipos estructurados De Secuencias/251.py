import numpy as np

# unidimensional board
raw = 20

board = np.zeros((raw), dtype=int)

board[9] = 1

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

        # test the last position
        if i + 2 == len(board) - 1:
            if board[i] == 0 and board[i + 1] == 0 and board[i + 2] == 0:
                newBoard[i] = 0
            if board[i] == 0 and board[i + 1] == 0 and board[i + 2] == 1:
                newBoard[i] = 1
            if board[i] == 0 and board[i + 1] == 1 and board[i + 2] == 0:
                newBoard[i] = 1
            if board[i] == 0 and board[i + 1] == 1 and board[i + 2] == 1:
                newBoard[i] = 0
            if board[i] == 1 and board[i + 1] == 0 and board[i + 2] == 0:
                newBoard[i] = 1
            if board[i] == 1 and board[i + 1] == 0 and board[i + 2] == 1:
                newBoard[i] = 1
            if board[i] == 1 and board[i + 1] == 1 and board[i + 2] == 0:
                newBoard[i] = 0
            if board[i] == 1 and board[i + 1] == 1 and board[i + 2] == 1:
                newBoard[i] = 0
            break

        # test the first position
        else:
            if board[i-1] == 0 and board[i] == 0 and board[i + 1] == 0:
                newBoard[i] = 0
            if board[i-1] == 0 and board[i] == 0 and board[i + 1] == 1:
                newBoard[i] = 1
            if board[i-1] == 0 and board[i] == 1 and board[i + 1] == 0:
                newBoard[i] = 1
            if board[i-1] == 0 and board[i] == 1 and board[i + 1] == 1:
                newBoard[i] = 0
            if board[i-1] == 1 and board[i] == 0 and board[i + 1] == 0:
                newBoard[i] = 1
            if board[i-1] == 1 and board[i] == 0 and board[i + 1] == 1:
                newBoard[i] = 1
            if board[i-1] == 1 and board[i] == 1 and board[i + 1] == 0:
                newBoard[i] = 0
            if board[i-1] == 1 and board[i] == 1 and board[i + 1] == 1:
                newBoard[i] = 0

    board = newBoard
    print('pulses', t + 1)
    for i in range(raw):
        if board[i] == 1:
            print('*', end='')
        else:
            print('.', end='')
