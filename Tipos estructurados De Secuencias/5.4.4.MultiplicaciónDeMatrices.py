import numpy as np

# pedimos la dimensión de la primera matriz y el número de columnas de la sengunda.

p = int(input('Dime el número de filas de A: '))
q = int(input('Dime el número de columnas de A (y filas de B): '))
r = int(input('Dime el número de filas de B: '))

# Creamos 2 matrices nulas.

A = np.zeros((p, q), dtype=int)
B = np.zeros((q, r), dtype=int)

# ...y leemos el contenido por tecládo.

print('Lectura de la matríz A: ')

for i in range(p):
    for j in range(q):
        A[i][j] = int(input(f'componente {i} {j}: '))

print('Lectura de la matríz B: ')

for i in range(p):
    for j in range(r):
        B[i][j] = int(input(f'componente {i} {j}: '))


C = A * B  # con numpy se puede multiplicar matrices fácilmente.

print('El resultado de la multiplicación de matrices es: ')

print(C)
