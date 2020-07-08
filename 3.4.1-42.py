#programa de cálculo de área y perímetro con solo 2 decimales.

from math import pi

#datos

radio = float(input('Radio: '))

#fórmula

perímetro = 2*pi*radio
área = pi * (radio**2)

print('El perímetro del circulo es de {0:.2f} metros, y su área es de {1:.2f} metros cuadrados.'.format(perímetro, área))
