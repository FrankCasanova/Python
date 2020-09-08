import numpy as np
from time import time
colum = 3  # int(imput('dame el número de columnas: /n '))
filas = 3  # int(imput('dame el número de filas: /n' ))

# creamos 2 listas nulas


a = np.zeros((colum, filas), dtype=int)
b = np.zeros((colum, filas), dtype=int)


for i in range(colum):
    for j in range(filas):
        a[i][j] = int(input(f'dame {i} y {j}: '))

print(a)


for i in range(colum):
    for j in range(filas):
        b[i][j] = int(input(f'dame {i} y {j}: '))

print(b)

suma = a + b

print(suma)
