# diseña un programa que lea una palabra y nos diga si es alfabética o no.

palabra = 'abcdfghi'  # input('Palabra: ')

i = 0
alfabética = True

while i < len(palabra)-1:
    if palabra[i] > palabra[i + 1]:
        alfabética = False
        break
    i += 1

if alfabética:
    print('Es una palabra alfabética')
else:
    print('No es una palabra alfabética')
