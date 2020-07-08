# programa que corrija el código binario mal formado.

bits = input('Introduzca un número binario: ')

check = 0

for i in bits:
    if i > '1' or i < '0':
        check += 1

while check > 0:

    check = 0

    bits = input('El número introducido es incorrecto, recuerda que un número binario solo puede contener unos y cero, Introduzca un número binario: ')
    for i in bits:
        if i > '1' or i < '0':
            check += 1

valor = 0

for i in bits:
    valor += valor + int(i)

print('Su valor en decimal es: ', valor)
