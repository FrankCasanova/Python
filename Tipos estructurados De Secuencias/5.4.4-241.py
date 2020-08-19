# programa que lea 2 matrices y calcule da diferencia entre la primera y la segunda.

filas = int(input('Número de filas:\n '))
columnas = int(input('Número de columnas:\n '))


a = [[0]*filas for i in range(filas)]
b = [[0]*filas for i in range(filas)]

for i in range(columnas):
    for j in range(filas):
        a[i][j] = int(input(f'Componentes {i}, {j} de a:\n'))

for i in range(columnas):
    for j in range(filas):
        b[i][j] = int(input(f'Componentes {i}, {j} de b:\n'))

c = [[0]*filas for i in range(filas)]

for i in range(columnas):
    for i in range(filas):
        c[i][j] = a[i][j] - b[i][j]

print('Diferencia')        

for i in range(columnas):
    for i in range(filas):
        print(c[i][j], end=' ')
    print()    
