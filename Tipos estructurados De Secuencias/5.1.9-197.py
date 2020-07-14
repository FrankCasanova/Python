# programa que lea una palabra y un entero, y muestre por pantalla todas sus subcadenas con valor K.

palabra = 'petardeando'

longitud = 3

#final = len(palabra) - longitud

if len(palabra) > longitud:

    for i in range(0, len(palabra) - (longitud-1)):
        print(palabra[i: i + longitud])
else:
    print('la longitud de las subpalabras no puede ser mayor a la palabra')
