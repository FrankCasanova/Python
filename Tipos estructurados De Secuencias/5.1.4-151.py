# programa que cuente el número de letras mayusculas que tiene una frase

frase = input('Escriba la Frase: ')

mayus = 0

for i in frase:
    if i >= 'A' and i <= 'Z':
        mayus += 1

print('La cantidad de mayusculas que tiene la frase es: ', mayus)
