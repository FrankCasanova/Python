#programa de cálculo del área de un triangulo dados 2 lados y el ángulo.

from math import sin, pi

#datos

ladoA = float(input('Lado A: '))
ladoB = float(input('Lado B: '))
ángulo = float(input('Ángulo : '))

#fórmula 

radianes = ángulo * (pi/180)
área = (1/2) * ladoA*ladoB*sin(radianes)

print('El área es de {0} metros cuadrados'.format(área))

