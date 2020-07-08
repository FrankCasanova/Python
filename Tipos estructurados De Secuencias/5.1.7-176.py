# convertir número de base octal a decimal

num = input('introduzca su número de base octal: ')

error = False

for i in num:
    if i > '7' or i < '0':
        error = True

while error == True:
    print('Recuerda que un número de base octal solo puede contener valores entre cero y siete.')
    num = input('introduzca su número de base octal: ')

    error = False

    for i in num:
        if i > '7' or i < '0':
            error = True

print('el número {0} en base octal es: {1}'.format(num, int(num, 8)))
