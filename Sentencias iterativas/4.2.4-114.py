#mejora del programa de los menús de diferentes calculos de un circulo

from math import pi

radio = int(input('Radio: '))

opción = ''
repetir = ''

while opción != 'd':

    if repetir == 'y':
        radio = int(input('Número: '))


    print('Escoge una opción: ')
    print('a) Calcular el diámetro.')
    print('b) Calcular el perímetro.')
    print('c) Calcular el área.')
    print('d) Finalizar')

    opción = input('teclea una opción: ')

    if opción == 'a':
        diámetro = 2*radio
        print('El diámetro es', diámetro)
        repetir = input('desea volver a calcularlo pero con un rádio distinto? teclea << y >> de ser así: ')

    elif opción == 'b':
        perímetro = 2*pi*radio
        print('El perímetro es', perímetro)
        repetir = input('desea volver a calcularlo pero con un rádio distinto? teclea << y >> de ser así: ') 

    elif opción == 'c':
        área = pi*radio**2
        print('El área es', área)
        repetir = input('desea volver a calcularlo pero con un rádio distinto? teclea << y >> de ser así: ')

    elif opción != 'd':
        print('Solo hay cuatro opciones: a, b, c o d. Tú has tecleado', opción)

print('Que tenga un buen día.')                
