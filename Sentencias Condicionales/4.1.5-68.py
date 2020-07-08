#testeo de programa de ecuación de segundo grado.

from math import sqrt

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

if a == 0:
    if b == 0:
        if c == 0:
            print('La ecuación tiene infinitas soluciones.')                   #EL PROGRAMA FUNCIONA IGUAL QUE EL DEL EJEMPLO
        else:
            print('La ecuación no tiene solución.')
    else:
        x = -c / b
        print('La solución es: x= {0:.3f}'.format(x))
else:
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    print('La la solución: x1={0:.3f} y x2=:{1:.3f}'.format(x1,x2))                    