# programa que lea una frase y un número y diga si todas son cortas si todas las palabras son más cortas que el número indicado
# de lo contrario que diga que hay alguna palabra larga.

frase = input('Escriba una frase: ')
num = int(
    input('Número que servirá para determinar si una palabras es larga o corta:  '))

while frase != '':
    contador = 0
    frase_larga = False
    for i in range(len(frase)):
        if frase[i] != ' ':
            contador += 1
            if i == len(frase) - 1 or frase[i + 1] == ' ':
                if contador >= num:
                    frase_larga = True
                    break
                else:
                    contador = 0

    if frase_larga:
        print('Existen palabras largas.')
        break
    else:
        print('Todas son cortas.')
        break
