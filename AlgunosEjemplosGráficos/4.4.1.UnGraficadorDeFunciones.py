# graficar fuciones.
from turtle import Screen, Turtle
from math import sin, pi

x1 = float(input('Dime el límite que estará más a la izquierda.'))
x2 = float(input('Dime el límite que estará más a la derecha.'))
puntos = int(input('Dame el número de puntos por los que pasará el gráfico.'))

pantalla = Screen()
pantalla.setup(825, 425)
pantalla.screensize(800, 400)
pantalla.setworldcoordinates(x1, -1, x2, 2)

tortuga = Turtle()
x = x1
px = (x2 - x1) / puntos

tortuga.penup()
tortuga.goto(x, sin(x1))
tortuga.pendown()
while x <= x2:
    tortuga.goto(x, sin(x))
    x += px

pantalla.exitonclick()
