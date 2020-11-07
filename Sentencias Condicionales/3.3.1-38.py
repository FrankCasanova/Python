#Programa de cálculo de área y perímetro de un triángulo.

from math import sqrt


#datos 

ladoA = float(input('Lado A: '))
ladoB = float(input('Lado B: '))
ladoC = float(input('Lado C: '))

#fórmulas

s = (ladoA+ladoB+ladoC) / 2

perímetro = ladoA + ladoB + ladoC

área = sqrt(s * ((s-ladoA) * (s-ladoB) * (s-ladoC)))

print('El perímetro es de {0} metros, y el área de {1} metros cuadrados'.format(perímetro, área))


