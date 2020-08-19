# Haz un programa que pida un entero positivo n y almacene en una variable M la 
# matriz identidad de n x n (la que tiene unos en diagonal principal y ceros en el resto de celdas)

n = int(input('Introduce la dimensión de la matriz (n x n)\n'))

M = [[0]*n for i in range(0,n)]

for i in range(len(M)):
    M[i][i] = 1

print(M)