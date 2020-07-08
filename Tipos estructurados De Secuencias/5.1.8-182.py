# diseña un programa que indique si la frase escrita es un palíndromo o no.

frase = input('Frase: ')

fraseInvertida = ''

for i in frase:
    fraseInvertida = i + fraseInvertida

if fraseInvertida == frase:
    print('La frase es palíndroma')
else:
    print('La frase NO es palíndroma')
