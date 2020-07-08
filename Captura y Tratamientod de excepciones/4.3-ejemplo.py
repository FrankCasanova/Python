# captura y tratamiento de excepciones

from math import sqrt

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

try:

    x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    if x1 == x2:
        print('Solución: x={0:.3f}'.format(x1))

    else:
        print('Solución: x1={0:.3f} y x2={1:.3f}'.format(x1, x2))

except ZeroDivisionError:
    if b != 0:
        print('La ecuación no tiene solución.')
    else:
        print('La ecuación tiene infinitas soluciones.')

except ValueError:
    print('No hay soluciones reales.')
