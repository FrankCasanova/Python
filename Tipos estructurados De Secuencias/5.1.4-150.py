# programa que cuente el número de espacios en blanco que tiene una cadena.

frase = input('Escriba la frase que quiere que se le cuenten los espacios: ')

espacios = 0

for i in frase:
    if i == ' ':
        espacios += 1

print('El número de espacios que tiene la frase es: {0}'.format(espacios))
