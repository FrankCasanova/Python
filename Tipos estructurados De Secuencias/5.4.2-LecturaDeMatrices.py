# si deseamos leer una matriz de tama;o determinado, podemos crear una matriz nula como 
# hemos visto en el apartado anteriory, a conticuación, rellenar cada uno de sus componentes.

#PEDIMOS LA DIMENSIÓN DE LA MATRIZ.

m = int(input('Dime el número de filas\n'))
n = int(input('Dime el número de columnas\n'))

#CREAMOS UNA MATRIZ NULA...

M = [[0]*n for i in range(m)]


# ... Y LEEMOS SU CONTENIDO DE TECLADO 
for i in range(m):
    for j in range(n):
        M[i][j] = float(input(f'Dame el componente{i}, {j}:\n'))
    

print(M)