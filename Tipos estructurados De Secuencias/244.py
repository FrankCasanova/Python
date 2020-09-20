# diseñar un programa que lea una matriz A de dimensión m x n y muestre un vector v de talla n.

# pedimos al usuario el tamaño de la matriz

import numpy as np

filas = 5  # int(input('Dame el número de filas: '))
columnas = 5  # int(input('Dame el número de columnas: '))

# creamos la matriz vacía

matriz = np.ones((filas, columnas), dtype=int)

print(matriz)

# for i in range(filas):
#     for j in range(columnas):
#         matriz[i][j] = input(f'dame el componente {i} {j}:  ')

vector = []

for i in range(columnas):
    for j in range(filas):
        vector.append(j * matriz[i][j])


print(vector)


print('la matriz ha quedado tal que así')
print(matriz)
