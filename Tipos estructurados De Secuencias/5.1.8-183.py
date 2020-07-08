# programa que diga si una frase es palíndroma obviando los espacios y los puntos.

frase = input('frase: ')

frase2 = ''
fraseInvert = ''


for i in frase:
    if i == ' ' or i == '.':
        pass
    else:
        frase2 += i

for i in frase2:
    fraseInvert = i + fraseInvert

if fraseInvert == frase2:
    print('La frase es palíndroma.')
else:
    print('La frase NO es palíndroma.')
