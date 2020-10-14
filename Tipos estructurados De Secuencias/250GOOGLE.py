from turtle import Screen, Turtle
print('Programa del juego de la vida toroidal.')


filas = 10  # int(input('Dime el número de filas: '))
columnas = 10  # int(input('Dime el número de colúmnas: '))

tablero = []
for i in range(filas):
    tablero.append([False]*columnas)

pantalla = Screen()
pantalla.setup(425, 425)
pantalla.screensize(400, 200)
pantalla.delay(0)

tablero[4][5] = True
tablero[5][5] = True
tablero[6][5] = True

# Preparar incrementos
dc = 30  # incremento en x
df = 30  # incremento en y

# Representar el tablero.

for y in range(filas):
    for x in range(columnas):
        if tablero[y][x]:
            célula = Turtle('square')
            célula.color('blue')
            célula.speed(0)
            célula.penup()
            célula.goto(x*dc, -y*df)
            célula.pendown()
        else:
            célula = Turtle('square')
            célula.color('red')
            célula.speed(0)
            célula.penup()
            célula.goto(x*dc, -y*df)
            célula.pendown()

pulsos = 6
for t in range(pulsos):
    # Preparar un nuevo tablero.
    nuevo = []
    for i in range(filas):
        nuevo.append([False]*columnas)
    # Actualizar el tablero.
    for y in range(filas):
        for x in range(columnas):
            # Calcular el número de vecinos de la celda que estamos visitando.
            n = 0
            if y > 0 and x > 0 and tablero[(y-1) % filas][(x-1) % columnas]:
                n += 1
            if x > 0 and tablero[y][(x-1) % columnas]:
                n += 1
            if y < filas-1 and x > 0 and tablero[(y+1) % filas][(x-1) % columnas]:
                n += 1
            if y > 0 and tablero[(y-1) % filas][x]:
                n += 1
            if y < filas-1 and tablero[(y+1) % filas][x]:
                n += 1
            if y > 0 and x < columnas-1 and tablero[y-1 % (filas)][x+1 % (columnas)]:
                n += 1
            if x < columnas-1 and tablero[y][(x+1) % columnas]:
                n += 1
            if y < filas-1 and x < columnas-1 and tablero[(y+1) % filas][(x+1) % columnas]:
                n += 1
            # Aplicar las reglas.
            if tablero[y][x] and (n == 2 or n == 3):  # Supervivencia.
                nuevo[y][x] = True
            elif not tablero[y][x] and n == 3:  # Nacimiento.
                nuevo[y][x] = True
            else:  # Superpoblación y aislamiento.
                nuevo[y][x] = False

            # célula.goto(n)

    # Actualizar el tablero.
    tablero = nuevo

    # Representar el tablero.
    print('Pulso', t+1)
    for y in range(filas):
        for x in range(columnas):
            if tablero[y][x]:
                célula = Turtle('square')
                célula.color('blue')
                célula.speed(0)
                célula.penup()
                célula.goto(x*dc, -y*df)
                célula.pendown()
            else:
                célula = Turtle('square')
                célula.color('red')
                célula.speed(0)
                célula.penup()
                célula.goto(x*dc, -y*df)
                célula.pendown()

pantalla.exitonclick()
