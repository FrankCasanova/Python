# PROGRAMA DE CALCULO DE VECTORES TRIDIMENSIONALES

from math import acos, pi, sqrt

opción = ''
vector1 = (0, 0, 0)
vector2 = (0, 0, 0)

while opción != '9':

    print('Escoge una opción.')
    print('1) Introducir el primer vector: ')
    print('2) Introducir el segundo vector: ')
    print('3) Calcular la suma: ')
    print('4) Cacular la diferencia: ')
    print('5) Calcular el producto escalar: ')
    print('6) Calcular el producto vectorial: ')
    print('7) Calcular el ángulo en grados entre ellos: ')
    print('8) Calcular la longitud: ')
    print('9) Finalizar: ')
    opción = (input('introduza una opción: '))

    if opción == '1':
        x1 = int(input('X del primer vector: '))
        y1 = int(input('Y del primer vector: '))
        z1 = int(input('Z del primer vector: '))
        vector1 = (x1, y1, z1)

    elif opción == '2':
        x2 = int(input('X del segundo vector: '))
        y2 = int(input('Y del segundo vector: '))
        z2 = int(input('Z del segundo vector: '))
        vector2 = (x2, y2, z2)

    elif opción == '3':

        if vector1 == (0, 0, 0) and vector2 == (0, 0, 0):
            print('Para realizar los calculos necesitamos que introduzca coordenadas.')

        elección = ''

        while elección == '':
            print('Elija en qué orden quiere sumarlos.')
            print('pulse 1 para sumar el primer vector al segundo vector.')
            print('pulse 2 para sumar el segundo vector al primer vector.')
            elección = input('Cual es su elección?: ')

            if elección == '1':
                suma = (x1 + x2), (y1 + y2), (z1 + z2)
                print(suma)
            elif elección == '2':
                suma = (x2 + x1), (y2 + y1), (z2 + z1)
                print(suma)
            elif elección != '1' and elección != '2':
                print('no ha elegido ninguna de las opciones disponibles')
                elección = ''

    elif opción == '4':

        if vector1 == (0, 0, 0) and vector2 == (0, 0, 0):
            print('Para realizar los calculos necesitamos que introduzca coordenadas.')

        else:
            resta = (x1 - x2), (y1 - y2), (z1 - z2)
            print(resta)

    elif opción == '5':

        if vector1 == (0, 0, 0) and vector2 == (0, 0, 0):
            print('Para realizar los calculos necesitamos que introduzca coordenadas.')

        else:
            escalar = (x1*x2) + (y1+y2) + (z1+z2)
            print(escalar)

    elif opción == '6':

        if vector1 == (0, 0, 0) and vector2 == (0, 0, 0):
            print('Para realizar los calculos necesitamos que introduzca coordenadas.')

        else:
            vectorial = ((y1*z2) - (z1*y2)), ((z1*x2) -
                                              (x1*z2)), ((x1*y2) - (y1*x2))
            print(vectorial)

    elif opción == '7':

        if vector1 == (0, 0, 0) and vector2 == (0, 0, 0):
            print('Para realizar los calculos necesitamos que introduzca coordenadas.')

        else:
            ángulo = (180/pi) * acos(((x1*x2) + (y1*y2) + (z1*z2)) /
                                     (sqrt((x1**2) + (y1**2) + (z1**2)) * (sqrt(x2**2) + (y2**2) + (z2**2))))
            print(ángulo)

    elif opción == '8':

        if vector1 == (0, 0, 0) and vector2 == (0, 0, 0):
            print('Para realizar los calculos necesitamos que introduzca coordenadas.')

        vector = ''
        while vector != '0' and (vector1 != (0, 0, 0) or vector2 != (0, 0, 0)):

            print('De cual venctor desea saber la longitud')
            print('pulsa 1 para elegir el primer vector')
            print('pulsa 2 para elegir el segundo vector')
            print('pulsa 0 para volver al menú principal')
            vector = input('elija vector: ')

            if vector == '1':
                longitud = sqrt((x1**2) + (y1**2) + (z1**2))
                print(longitud)

            elif vector == '2':
                longitud = sqrt((x2**2) + (y2**2) + (z2**2))
                print(longitud)

            elif vector == '0':
                print('ok')
        else:
            print('de vuelta al menú principal.')

    elif opción == '9':
        print('Que tenga un buen día.')

    elif opción > '9' or opción < '1':
        print('debe teclear una opción disponible')

print('Adiós.')
