from turtle import Screen, Turtle


def koch(turttle, lenght, level):
    """
    docstring
    """
    if level == 0:
        turttle.forward(lenght)
    else:
        koch(turttle, lenght/3, level-1)
        turttle.left(40)
        koch(turttle, lenght/3, level-1)
        turttle.right(160)
        koch(turttle, lenght/3, level-1)
        turttle.left(120)
        koch(turttle, lenght/3, level-1)


def copo(turt, length, level):
    koch(turt, length, level)
    turt.right(120)
    koch(turt, length, level)
    turt.right(120)
    koch(turt, length, level)


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
copo(turtle, 500, 4)
screen.exitonclick()
