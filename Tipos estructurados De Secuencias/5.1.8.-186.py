# programa que solicite el nombre de un ficehero y muestre por pantalla los caracteres que forman su extensión.

fichero = input('Indique el nombre del fichero: ')

i = 0
tipoArchivo = ''

while i < len(fichero) - 1:
    try:
        if fichero[i] == '.' and fichero[i + 1] == 't' and fichero[i + 2] == 'e' and fichero[len(fichero)-1] == 'x':

            tipoArchivo += fichero[i + 1]
            tipoArchivo += fichero[i + 2]
            tipoArchivo += fichero[i + 3]
            break
    except IndexError:
        break
    try:
        if fichero[i] == '.' and fichero[i + 1] == 'd' and fichero[i + 2] == 'o' and fichero[len(fichero)-1] == 'c':

            tipoArchivo += fichero[i + 1]
            tipoArchivo += fichero[i + 2]
            tipoArchivo += fichero[i + 3]
            break
    except IndexError:
        break

    i += 1

if tipoArchivo == 'tex' or tipoArchivo == 'doc':
    print('El archivo es un archivo tipo: ', tipoArchivo)
else:
    print('no es un tipo de archivo')
