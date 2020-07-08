# lo mismo que en el ejercicio anterior pero dibujando el eje de cordenadas


from turtle import Turtle, Screen

a = int(input('Valor de a: '))
b = int(input('Valor de b: '))
c = int(input('Valor de c: '))

z1 = int(input('coordenada más a la izquierda en el eje x: '))
z2 = int(input('coordenada más a la derecha en el eje x: '))

y1 = ((a * z1) ** 2) + (b * z1) + c
y2 = ((4 * a * c) - (b ** 2)) / 4 * a

pantalla = Screen()
pantalla.setup(1025, 825)
pantalla.screensize(1000, 800)

if a > 0:
    pantalla.setworldcoordinates(z1, y2, z2, y1)
else:
    pantalla.setworldcoordinates(z1, y1, z2, y2)

t = Turtle()
t.penup()
t.goto(z1, (y1/2))
t.pendown()
t.goto(z2, (y1/2))
t.penup()
t.goto(0, y1)
t.pendown()
t.goto(0, y2)
t.penup()

t.goto(z1, ((a * z1) ** 2) + (b * z1) + c)

dx = (z2 - z1) / 300

x = z1

TOKEN = 1
TOKEN2 = 1
t.pencolor('blue')
t.pendown()
while x < z2:
    y = ((a * x) ** 2) + (b * x) + c
    if ((a * x) ** 2) + (b * x) + c <= y1 / 2 and TOKEN > 0:
        t.penup()
        t.goto(x, (y1/2))
        t.pendown()
        t.pencolor('red')
        t.dot(20)
        t.penup()
        t.pencolor('blue')
        t.goto(x,y)
        TOKEN -= 1
        t.pendown()
    
    if x > 0 and ((a * x) ** 2) + (b * x) + c >= y1 / 2 and TOKEN2 > 0:
        t.penup()
        t.goto(x, (y1/2))
        t.pendown()
        t.pencolor('red')
        t.dot(20)
        t.penup()
        t.pencolor('blue')
        t.goto(x,y)
        TOKEN2 -= 1
        t.pendown()

    #if x     
    t.goto(x, y)
    x += dx


pantalla.exitonclick()
