# these 2 mutually recursive functions
# define another interesting fractal structure
# the so-called dragon curve.
from turtle import Screen, Turtle
from math import sqrt


def drago(tur, lenght, level):
    """
    docstring
    """
    if level == 0:
        tur.forward(lenght)
    else:
        tur.right(45)
        drago(tur, lenght/sqrt(2), level-1)
        tur.left(90)
        nogard(tur, lenght/sqrt(2), level-1)
        tur.right(45)


def nogard(tur, lenght, level):
    """
    docstring
    """
    if level == 0:
        tur.forward(lenght)
    else:
        tur.left(45)
        drago(tur, lenght/sqrt(2), level-1)
        tur.right(90)
        nogard(tur, lenght/sqrt(2), level-1)
        tur.left(45)
    pass


screen = Screen()
screen.setup(1000, 1000)
screen.screensize(1000, 1000)
screen.setworldcoordinates(0, -350, 500, 150)
turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.goto(250, 0)
turtle.pendown()
turtle.speed(0)
nogard(turtle, 100, 11)
screen.exitonclick()
