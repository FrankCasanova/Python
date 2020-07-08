#determinar cual de las cordenadas es la más cercana a la primera cordenada.

from math import sqrt

x1 = int(input('por favor, eje de abcisa x1: '))
y1 = int(input( 'por favor eje de ordenada y1'))

x2 = int(input('por favor, eje de abcisa x2: '))
y2 = int(input( 'por favor eje de ordenada y2: '))

x3 = int(input('por favor, eje de abcisa x3: '))
y3 = int(input( 'por favor eje de ordenada y3: '))

x4 = int(input('por favor, eje de abcisa x4: '))
y4 = int(input( 'por favor eje de ordenada y4: '))

x5 = int(input('por favor, eje de abcisa x5: '))
y5 = int(input( 'por favor eje de ordenada y5: '))

cordenada1 = (x1, y1)
cordenada2 = (x2, y2)
cordenada3 = (x1, y3)
cordenada4 = (x4, y4)
cordenada5 = (x5, y5)


distancia1 = sqrt((x1 - x2)**2 + (y1 - y2)**2)
distancia2 = sqrt((x1 - x3)**2 + (y1 - y3)**2)
distancia3 = sqrt((x1 - x4)**2 + (y1 - y4)**2)
distancia4 = sqrt((x1 - x5)**2 + (y1 - y5)**2)

if distancia1 < distancia2 and distancia1 < distancia3 and distancia1 < distancia4:
    cercano = cordenada2
if distancia2 < distancia1 and distancia2 < distancia3 and distancia2 < distancia4:
    cercano = cordenada3
if distancia3 < distancia1 and distancia3 < distancia2 and distancia3 < distancia4:
    cercano = cordenada4
if distancia4 < distancia1 and distancia4 < distancia2 and distancia4 < distancia3:
    cercano = cordenada5

print('la coordenada {0} es la más cercana a la cordenada {1}'.format(cercano, cordenada1))                

