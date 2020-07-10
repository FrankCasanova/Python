# ejemplo del libro

frase = input('Escriba una frase: ').lower()

i = int(input('Dame un número: '))
j = int(input('Dame otro número: '))

# primera adición según el libro.

if j > len(frase):
    final = len(frase)

else:
    final = j


subFrase = ''

for k in range(i, final):
    subFrase += frase[k]

print('La subfrase entre {0} y {1} es {2}.'.format(i, j, subFrase))
