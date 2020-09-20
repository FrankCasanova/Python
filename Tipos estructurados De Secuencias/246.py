# diseña un programa que, dada una matriz, determine si la suma de los elementos de cualquiera de sus filas
# es igual a la suma de cualquiera de los elementos de cualquiera de sus columnas

import numpy as np

matriz = np.array([[4, 4, 2, 4, 5, 3], [5, 9, 4, 5, 6, 2],
                   [9, 1, 3, 1, 1, 7]], dtype=int)

algunas = False

for i in range(len(matriz)):
    if algunas:
        break
    else:
        for j in range(len(matriz[i])):
            if np.sum(matriz[i:i+1, :]) == np.sum([matriz[:, j:j + 1]]):

                algunas = True
                break


print(algunas)
