# Have the game of life program ask the user for the number of living neighbor
# cells needed for the different rules to fire and show how the board evolves with them

# original code update v2.

import numpy as np
from turtle import Screen, Turtle

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

nbToActivate = 2  # int(input('Number of neighbor cells need to live:\n\n'))

# prepare the increments

increY = 30
increX = 30

# prepare the Screen

screen = Screen()
screen.setup(725, 725)
screen.screensize(700, 700)
screen.setworldcoordinates(0, -700, 700, 0)

# representing board

for y in range(raws):
    for x in range(colums):
        if board[y][x]:
            cell = Turtle('square')
            cell.color('blue')
            cell.speed(0)
            cell.penup()
            cell.goto(x * increX, -y * increY)
            cell.pendown()
        else:
            cell = Turtle('square')
            cell.color('red')
            cell.speed(0)
            cell.penup()
            cell.goto(x * increX, -y * increY)
            cell.pendown()


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
            if y > 0 and x > 0 and board[(y-1) % raws][(x-1) % colums]:
                n += 1
            if x > 0 and board[y][(x-1) % colums]:
                n += 1
            if y < raws-1 and x > 0 and board[(y+1) % raws][(x-1) % colums]:
                n += 1
            if y > 0 and board[(y-1) % raws][x]:
                n += 1
            if y < raws-1 and board[(y+1) % raws][x]:
                n += 1
            if y > 0 and x < colums-1 and board[y-1 % (raws)][x+1 % (colums)]:
                n += 1
            if x < colums-1 and board[y][(x+1) % colums]:
                n += 1
            if y < raws-1 and x < colums-1 and board[(y+1) % raws][(x+1) % colums]:
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
    print('Pulse', t+1)
    for y in range(raws):
        for x in range(colums):
            if board[y][x]:
                cell = Turtle('square')
                cell.color('blue')
                cell.speed(0)
                cell.penup()
                cell.goto(x*increX, -y*increY)
                cell.pendown()
            else:
                cell = Turtle('square')
                cell.color('red')
                cell.speed(0)
                cell.penup()
                cell.goto(x*increX, -y*increY)
                cell.pendown()

screen.exitonclick()
