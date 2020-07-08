# programa de calculo de ecuaciones de segundo grado.

# EJEMPLAR

from math import sqrt

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

if a != 0:
    discriminante = b**2 - 4*a*c
    if discriminante >= 0:
        x1 = (-b + sqrt(discriminante)) / (2*a)
        x2 = (-b - sqrt(discriminante)) / (2*a)
        if x1 == x2:
            print('La solución: x= {0:.3f}'.format(x1))
        else:
            print('Soluciones: x1={0:.3f} y x2={1:.3f}'.format(x1, x2))

    else:
        print('No hay soluciones reales.')
else:
    if b != 0:
        x = -c / b
        print('Solución: x={0:.3f}'.format(x))
    else:
        if c != 0:
            print('La ecuación no tiene solución')
        else:
            print('La ecuación tiene infinitas soluciones.')
