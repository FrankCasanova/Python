# programa que muestre la cantidad de números introducidos por teclado.

text = input('Introduzca un texto: ')

token = 0

for i in range(len(text)):

    if text[i] >= '0' and text[i] <= '9':

        if i == len(text)-1 or text[i+1] == ' ':  # contador de números.

            token += 1


print('El texto tiene {0} números'.format(token))
