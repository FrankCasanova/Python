# programa que dado 3 valores a, b y c, muestre la función f(x) ax2 + bx + c
# en el intervalo z1 y z2, donde z1 y z2 son proporcionados por el usuario
# el programa debe calcular el máximo y el mínimo de fx para ajustar dicho valor en la pantalla.

from turtle import Turtle, Screen

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))


z1 = float(input('Valor del eje x más a la izquierda: '))
z2 = float(input('Valor del eje x más a la derecha: '))

y1 = ((a * z1) ** 2) + (b * z1) + c

if a > 0:
    y2 = ((4 * a * c) - (b ** 2)) / 4 * a
else:
    y2 = ((4 * a * c) - (b ** 2)) / 4 * a

pantalla = Screen()
pantalla.setup(825, 625)
pantalla.screensize(800, 600)

if a > 0:
    pantalla.setworldcoordinates(z1, y1, z2, y2)
else:
    pantalla.setworldcoordinates(z1, y2, z2, y1)

dx = (z2 - z1) / 100

t = Turtle()

t.penup()
t.goto(z1, (((a * z1) ** 2) + (b * z1) + c))
t.pendown()

x = z1

while x < z2:
    t.goto(x, (((a * x) ** 2) + (b * x) + c))
    x += dx

pantalla.exitonclick()
