# una matriz cuadrada es triangular superior si todos sus elementos por debajo de la diagonal son nulos.
# diseña un programa que diga si una matriz es diagonal o no.

import numpy as np

matriz = np.array([[1, 4, 3, 5, 6], [0, 5, 3, 8, 3], [0, 0, 3, 6, 4], [
                  0, 0, 0, 9, 6], [0, 0, 0, 0, 4]], dtype=int)

print(matriz)

diag = True

for i in range(len(matriz)):
    if i == 0:
        continue
    if diag == False:
        break
    for j in range(0, i):
        print(matriz[i][j], matriz[i][j+1])
        if matriz[i][i] == 0 or matriz[i][j] != 0:
            diag = False
            break


if diag:
    print('la matriz es triangular.')
else:
    print('la matriz NO es triangular.')
