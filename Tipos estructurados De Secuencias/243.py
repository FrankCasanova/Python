# La transpuesta de una matriz A de dimensíon m x n es una matriz At de dimensión
# n x m tal que Atij = Aji

import numpy as np

matriz = np.array(([1, 2, 3], [2, 12, 6], [1, 0, -3], [10, -1, 0]), dtype=int)

matrizTranspuesta = np.transpose(matriz)

print('La matriz sin transponer tendría esta forma: ')
print('-------------------------------------------')
print(matriz)
print('Una vez se transpone la matriz queda tal que así: ')
print('------------------------------------------------')


print(matrizTranspuesta)

print('como se puede ver los número de las filas se cambian a las columnas')
