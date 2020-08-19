# programa que lea una matriz y un número y devuelva una nueva matriz:
# la que resulta de multiplicar la matriz por el número.
# (el producto de un número por una matriz es la matriz que resulta de multiplicar cada elemento por dicho número.)

filas = int(input('Número de filas:\n'))
columnas = int(input('Número de columnas:\n'))

num = int(input('Número por el que desea multiplicar la matriz:\n'))

matriz = [[0]*filas for i in range(filas)]

for i in range(columnas):
    for j in range(filas):
        matriz[i][j] = int(input(f'componente {i}, {j}:\n'))

productoMatriz = [[0]*filas for i in range(filas)]

for i in range(columnas):
    for j in range(filas):
        productoMatriz[i][([j]*num)]


for i in range(columnas):
    for j in range(filas):
        print(productoMatriz[i][j], end=' ')
    print()            
    