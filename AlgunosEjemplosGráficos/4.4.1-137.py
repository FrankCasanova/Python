# programa que represente gunciones gráficamente.

from turtle import Screen, Turtle

x = -2
y = 1 / (x + 1)
puntos = 100

pantalla = Screen()
pantalla.setup(825, 625)
pantalla.screensize(800, 600)
pantalla.setworldcoordinates(-2, -25, 2, 5)


t = Turtle()

t.penup()
t.goto(x, (1/x+1))

dx = 4/100

while x <= 1:

    if x >= 0:
        t.pencolor('red')
        t.dot
        break

    t.pendown()
    t.goto(x, (1 / x + 1))
    x += dx


pantalla.exitonclick()
