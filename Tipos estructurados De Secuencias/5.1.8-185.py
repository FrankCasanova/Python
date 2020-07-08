# haz un programa que en cada vocal de la frase ponga un punto.

frase = input('Frase: ')

encrip = ''

for i in frase:
    if i == 'a' or i == 'á' or i == 'e' or i == 'é' or i == 'i' or i == 'í' or i == 'o' or i == 'ó' or i == 'u' or i == 'ú' or i == 'ü':
        encrip += '.'
    else:
        encrip += i

print('La frase encriptada es: ', encrip)

print('Gracias por usar nuestra aplicación.')
