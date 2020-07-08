# programa para comprobar si los parentesis están bien puesto.

frase = input('Escriba una frase con parentesis: ')

while frase != '':

    parentesis = 0

    for i in range(len(frase)):

        if frase[i] == '(':
            parentesis += 1

        if frase[i] == ')':
            parentesis -= 1

    if parentesis == 0:
        print('La frase está bien parentizada')
        break

    else:
        print('La frase está mal parentizada')
        break

print('Adiós.')
