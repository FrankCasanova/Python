from turtle import Screen, Turtle
from math import cos

x1 = float(input('Valor más a la izquierda de la pantalla: '))
x2 = float(input('Valor más a la derecha de la pantalla: '))
puntos = float(
    input('Numero de puntos desde el punto inicial hasta el final: '))

pantalla = Screen()
pantalla.setup(825, 425)
pantalla.screensize(800, 400)
pantalla.setworldcoordinates(x1, -1, x2, 1)

tortuga = Turtle()
x = x1
px = (x2 - x1) / puntos

tortuga.penup()
tortuga.goto(x, cos(x))
tortuga.pendown()
while x <= x2:
    tortuga.goto(x, cos(x))
    x += px

pantalla.exitonclick()
