#programa de cáclulo de área y perímetro de rectangulo

#datos

LadoA = float(input('Lado A: '))
ladoB = float(input('Lado B: '))

#fórmula

perímetro = LadoA*2 + ladoB*2
área = LadoA*ladoB

print('El perímetro es de {0} y el área de {1}'.format(perímetro, área))