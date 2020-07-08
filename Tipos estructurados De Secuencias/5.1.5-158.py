# programa que lea una frase y un número y nos digas cuantas palabras tiene la longitud del número

frase = input('Escriba la frase: ')
num = int(input('Encontrar palabras con una longitud de: '))

while frase != '':
    match = 0
    contador = 0

    for i in range(1, len(frase)):
        if frase[i] != ' ':
            contador += 1
            if frase[i] == frase[len(frase) - 1] or frase[i + 1] == ' ':
                if contador == num:
                    match += 1
                    contador = 0
                else:
                    contador = 0

    print('El número de palabras con {0} letras es:{1} '.format(num, match))
    break
