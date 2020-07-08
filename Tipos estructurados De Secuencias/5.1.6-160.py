# programa que nos diga si todas las palabras tienen una longitud de "x" caracteres.


try:
    frase = input('Escriba la frase: ')
    num = int(input('Deme el número: '))

except ValueError:

    print('El valor tiene que ser un número.')
    num = int(input('Deme el número: '))

todas = False
match = False

while todas == False and frase != '':
    contador = 0
    for i in range(len(frase)):
        if frase[i] != ' ':
            contador += 1
            if i == len(frase)-1 or frase[i + 1] == ' ':
                if contador == num:
                    match = True
                    contador = 0
                    todas = True
                else:
                    todas = False
                    break
    if todas:
        print(
            'Todas las palabras tienen una longitud de {0} carácteres'.format(num))
        break
    else:
        print(
            'No todas las palabras tienen una logitud de {0} carácteres'.format(num))
        break
