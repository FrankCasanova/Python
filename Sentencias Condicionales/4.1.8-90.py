#CORRECCIÓN DE PROGRAMA.
from math import pi

radio = float(input('Dame el radio de un circulo: '))

#menú
print('Escoge una opción: ')
print('a) Calcular el diámetro: ')
print('b) Calcular el perímetro: ')
print('c) Calcular el área: ')

opción = input('Teclea a, b o c y pulsa intro: ')

if opción.lower() == 'a':
    diámetro = 2*pi
    print('El diámetro es {0}'.format(diámetro))

else:
    if opción.lower() == 'b':
        perímetro = 2*pi*radio
        print('El perímetro es {0}'.format(perímetro))
    else:
        if opción.lower() == 'c':
            área = pi*radio**2
            print('El área es {0}'.format(área))
        else:
            print('Solo hay 3 opciónes: a, b o c.')
            print('Tú has tecleado {0}'.format(opción))         