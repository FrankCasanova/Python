# ejemplo de inversión de cadena.

frase = input('introduca la frase: ')

invert = ''

for i in frase:
    invert = i + invert

print('La inversión de la frase escrita es: ', invert)
