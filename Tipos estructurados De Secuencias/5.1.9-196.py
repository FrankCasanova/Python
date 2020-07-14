# programa que lea una palabra y lea sus subpalabras de longitud 3.

palabra = 'petardeando'  # input('Palabra: ')

final = len(palabra)-3

for i in range(0, len(palabra) + 1):

    if i == final:
        break
    else:
        print(palabra[i:i+3])
