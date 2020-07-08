# programa que lea una frase y un número y determine si todas las palabras son largas o si hay alguna corta.

frase = input('Escriba la frase: ')
num = int(input('Número de referencia: '))

while frase != '':

    hay_cortas = False
    contador = 0

    for i in range(len(frase)):
        if frase[i] != ' ':
            contador += 1
            if i == len(frase) - 1 or frase[i + 1] == ' ':
                if contador < num:
                    hay_cortas = True
                    break
                else:
                    contador = 0

    if hay_cortas:
        print('Hay alguna palabra corta.')
        break
    else:
        print('Todas las palabras son largas.')
        break
