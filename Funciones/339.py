# implements memorión3, a variant of memorión in which
# you have to match groups of 3 equal letters.
# (make sure the number of cells in the matrix
# is a multiple of 3)

from os import TMP_MAX
from random import randrange
from turtle import Screen, Turtle
from time import sleep


closed_cell = 0
open_cell = 1
temp_open_cell = 2


def menu():
    """
    game menu
    """
    global raws, columns

    print('bienvenido al juego Memorión.')
    print('Elije la dificultad del juego:')
    while (option := input('pulsa: a. para dificultad: Easy\n pulsa: b. para dificultad: noraml.\n pulsa: c. para dificultad: hard.')):
        if option == 'a':
            raws = 3
            columns = 4
            break
        elif option == 'b':
            raws = 4
            columns = 6
            break
        elif option == 'c':
            raws = 6
            columns = 8
            break

        else:
            print('no has elegido una opción correcta.')
            continue


def make_matrix(raws, columns):
    '''
    that build a matrix
    >>> make_matrix(3,3)
    [[None, None, None], [None, None, None], [None, None, None]]
    '''

    return [[None]*columns for i in range(raws)]


def start_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = closed_cell


def fill_symbol(symbol):
    num_symbol = 0
    for i in range(len(symbol)):
        for j in range(len(symbol[0])):
            symbol[i][j] = chr(ord('a') + num_symbol//3)
            num_symbol += 1

    for i in range(1000):
        [f1, c1] = [randrange(len(symbol)), randrange(len(symbol[0]))]
        [f2, c2] = [randrange(len(symbol)), randrange(len(symbol[0]))]
        [f3, c3] = [randrange(len(symbol)), randrange(len(symbol[0]))]

        tmp = symbol[f1][c1]
        symbol[f1][c1] = symbol[f2][c2]
        symbol[f2][c2] = symbol[f3][c3]
        symbol[f3][c3] = tmp


def draw_board(board, symbol):
    for i in range(len(symbol)):
        for j in range(len(symbol[0])):
            draw_cell(board, symbol, i, j)


def draw_cell(tile, symbol, i, j):
    global turtle
    turtle.penup()
    turtle.goto(j+.5, i)
    turtle.begin_fill()
    if tile[i][j] == closed_cell:
        turtle.fillcolor('blue')
        turtle.circle(.5)
    elif tile[i][j] == open_cell:
        turtle.fillcolor('white')
        turtle.circle(.5)
        turtle.goto(j+.5, i+.25)
        turtle.write(symbol[i][j])
    else:
        turtle.fillcolor('yellow')
        turtle.circle(.5)
        turtle.goto(j+.5, i+.25)
        turtle.write(symbol[i][j])

    turtle.end_fill()
    turtle.pendown()


def clic(x, y):
    global board, symbol, temp2, temp1, temp3
    screen.onclick(None)

    [j, i] = [int(x), int(y)]

    if 0 <= i < len(board) and 0 <= j < len(board[0]):
        if board[i][j] == closed_cell:
            if temp1 == None:
                temp1 = [i, j]
                board[i][j] = temp_open_cell

            elif temp2 == None:
                temp2 = [i, j]
                board[i][j] = temp_open_cell

            else:
                temp3 = [i, j]
                board[i][j] = temp_open_cell

            draw_cell(board, symbol, i, j)

            if temp3 != None:
                if symbol[temp1[0]][temp1[1]] == symbol[temp2[0]][temp2[1]] == symbol[temp3[0]][temp3[1]]:

                    board[temp1[0]][temp1[1]] = open_cell
                    board[temp2[0]][temp2[1]] = open_cell
                    board[temp3[0]][temp3[1]] = open_cell
                else:
                    sleep(0.7)
                    board[temp1[0]][temp1[1]] = closed_cell
                    board[temp2[0]][temp2[1]] = closed_cell
                    board[temp3[0]][temp3[1]] = closed_cell

                draw_cell(board, symbol, temp1[0], temp1[1])
                draw_cell(board, symbol, temp2[0], temp2[1])
                draw_cell(board, symbol, temp3[0], temp3[1])

                temp1 = None
                temp2 = None
                temp3 = None

        draw_cell(board, symbol, i, j)

    if all_open(board):
        screen.bye()
    else:
        screen.onclick(clic)


def all_open(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == closed_cell:
                return False
    return True


temp1 = None
temp2 = None
temp3 = None


# MAIN
raws = None
columns = None

menu()
screen = Screen()
screen.setup(columns*50, raws*50)
screen.screensize(columns*50, raws*50)
screen.setworldcoordinates(-.5, -.5, columns+.5, raws+.5)
screen.delay(0)
turtle = Turtle()
turtle.hideturtle()

symbol = make_matrix(raws, columns)
board = make_matrix(raws, columns)

start_board(board)
fill_symbol(symbol)
draw_board(board, symbol)

screen.onclick(clic)
screen.mainloop()

screen.exitonclick()
