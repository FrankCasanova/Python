# graficar una simulación gravitacional. (#necesario para el bot supremo, no solo de albión, sino de cualquier juego.)

from turtle import Screen, Turtle
from math import sqrt

# pantalla
pantalla = Screen()
pantalla.setup(1025, 1025)
pantalla.screensize(1000, 1000)
pantalla.setworldcoordinates(-500, -500, 500, 500)
pantalla.delay(0)

# cuerpo 1
x1 = -200
y1 = -200
velocidad_x1 = 0.1
velocidad_y1 = 0.0
m1 = 20

# cuerpo 2
x2 = 200
y2 = 200
velocidad_x2 = -0.1
velocidad_y2 = 0.0
m2 = 10

# cuerpo 3
x3 = 200
y3 = -50
velocidad_x3 = 0.1
velocidad_y3 = 0.0
m3 = 50

# graf.masa1
cuerpo1 = Turtle('circle')
cuerpo1.color('red')
cuerpo1.speed(0)
cuerpo1.penup()
cuerpo1.goto(x1, y1)
cuerpo1.pendown()

# graf.masa2
cuerpo2 = Turtle('circle')
cuerpo2.color('blue')
cuerpo2.speed(0)
cuerpo2.penup()
cuerpo2.goto(x2, y2)
cuerpo2.pendown()

# graf.masa3
cuerpo3 = Turtle('circle')
cuerpo3.color('purple')
cuerpo3.speed(0)
cuerpo3.penup()
cuerpo3.goto(x3, y3)
cuerpo3.pendown()

while x1 != x2:

    # formulas

    r = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (x3 - x1)**2 +
             (y3 - y1)**2 + (x3 - x2)**2 + (y3 - y2)**2)

    r3 = r**3

    aceleración_x1 = (m2 + m3) * ((x2-x1) + (x3-x1)) / r3
    aceleración_y1 = (m2 + m3) * ((y2-y1) + (y3-y1)) / r3
    aceleración_x2 = (m1 + m3) * ((x1-x2) + (x3-x2)) / r3
    aceleración_y2 = (m1 + m3) * ((y1-y2) + (y3-y2)) / r3
    aceleración_x3 = (m1 + m2) * ((x1-x3) + (x2-x3)) / r3
    aceleración_y3 = (m1 + m2) * ((y1-y3) + (y2-y3)) / r3

    velocidad_x1 += aceleración_x1
    velocidad_y1 += aceleración_y1
    velocidad_x2 += aceleración_x2
    velocidad_y2 += aceleración_y2
    velocidad_x3 += aceleración_x3
    velocidad_y3 += aceleración_y3

    x1 += velocidad_x1
    y1 += velocidad_y1
    x2 += velocidad_x2
    y2 += velocidad_y2
    x3 += velocidad_x3
    y3 += velocidad_y3

    cuerpo1.goto(x1, y1)
    cuerpo2.goto(x2, y2)
    cuerpo3.goto(x3, y3)

pantalla.exitonclick()
