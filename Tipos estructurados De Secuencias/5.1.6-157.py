# programa del alumno aventajado

cadena = input('Escribe una frase: ')
while cadena != '':
    cambios = 0
    for i in range(1, len(cadena)):
        if cadena[i] == ' ' and cadena[i - 1] != ' ':
            cambios = cambios + 1

    if cadena[-1] == ' ':
        cambios -= 1

    palabras = cambios + 1

    print('Palabras: ', palabras)
    cadena = input('Escribe una frase: ')
