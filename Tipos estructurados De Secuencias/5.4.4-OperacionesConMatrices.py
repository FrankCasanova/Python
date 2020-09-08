# Pedimos la dimensión de las matrices.

m = int(input('Dime el número de filas:\n'))
n = int(input('Dime el número de columnas:\n'))

# Creamos 2 matrices nulas...

a = [[0]*n for i in range(m)]
b = [[0]*n for i in range(m)]

# ... y leemos sus contenidos de teclado.
print('Lectura de la matriz a.')
for i in range(m):
    for j in range(n):
        a[i][j] = float(input(f'Componente {i}, {j}:\n '))

print('Lectura de la matriz b.')
for i in range(m):
    for j in range(n):
        b[i][j] = float(input(f'Componente {i}, {j}:\n '))

# Construimos la matriz en la que queremos albergar el resultado.

c = [[0]*n for i in range(m)]

for i in range(m):
    for j in range(n):
        c[i][j] = a[i][j] + b[i][j]

# Mostramos el resultado por pantalla
print('Suma: ')
for i in range(m):
    for j in range(n):
        print(c[i][j], end=' ')
    print()
