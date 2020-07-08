# programa que indique si hay palabras largas dependiendo del número que indique el usuario

frase = input('Deme una frase: ')
num = int(input('Deme un número: '))

largas = False

while largas == False and frase != '':
    contador = 0

    for i in range(len(frase)):
        if frase[i] != ' ':
            contador += 1
            if i == len(frase) - 1 or frase[i + 1] == ' ':
                if contador > num:
                    largas = True
                    break
                else:
                    contador = 0

    if largas:
        print('Éxisten palabras largas')
        break
    else:
        print('No existen palabras largas')
        break
