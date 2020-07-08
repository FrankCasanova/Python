# ejemplo contador de palabras

# versión 1.0
#frase = input('Escribe una frase: ')

# while frase != '':
#     blancos = 0
#     for i in frase:
#         if i == ' ':
#             blancos += 1
#     palabras = blancos + 1
#     print('Palabras: ', palabras)

#     frase = input('Escribe una frase: ')

# versión 2.0
# frase = input('Escribe la frase: ')

# while frase != '':

#     cambios = 0
#     anterior = ''
#     for i in frase:
#         if i == ' ' and anterior != ' ':
#             cambios += 1
#         anterior = i

#     palabras = cambios + 1  # hay una palabra más que cambios de no blanco a blanco

#     print('Palabras: ', palabras)
#     frase = input('Escribe la frase: ')

# versión3.0

frase = input('Escribe una frase: ')

while frase != '':
    cambios = 0
    anterior = ' '  # version 3.1 era añadir como valor por defecto el caracter "espacio"

    for i in frase:
        if i == ' ' and anterior != ' ':
            cambios += 1
        anterior = i

    if frase[-1] == ' ':
        cambios -= 1

    palabras = cambios + 1
    print('Palabras: ', palabras)
    frase = input('Escribe una frase: ')
