# programa que nos diga el número de palabras igual al carácter indicado

frase = input('Escriba la frase: ')
num = int(input('Valor que determina si la frase es mayor o menor: '))

algunas = False
ejecutado = False
while ejecutado == False and algunas == False and frase != '':

    contador = 0

    for i in range(1, len(frase)):
        ejecutado = True
        if frase[i] != ' ':
            contador += 1
            if frase[i] == frase[len(frase) - 1] or frase[i + 1] == ' ':
                if contador == num:
                    algunas = True
                    break

if not algunas:
    print('La frase no tiene ninguna palabra igual al número indicado.')

else:
    print('La frase tiene alguna palabra de igual longitud al número indicado')
