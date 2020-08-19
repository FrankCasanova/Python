# Crea una matriz utilizando la técnica del bucle descrita anteriormente.

M = [[0]*4 for i in range(0,4)]
print()

for i in range(len(M)):
    M[i][i] = 1

print(M)    


