# programa como el del ejemplo pero que base el cómputo en transiciones de blanco a no blanco

frase = input('Escribe una frase: ')

while frase != '':
    cambios = 0

    for i in range(len(frase)-1, -1, -1):
        if frase[i] == ' ' and frase[i - 1] != ' ':
            cambios += 1

    if frase[-1] == ' ':
        cambios -= 1

    palabras = cambios + 1
    print('Palabras: ', palabras)
    frase = input('Escribe una frase: ')
