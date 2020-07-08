# convertir número hexadecimal introducido a decimal.

num = input('Introduzca un número hexadecimal: ')

error = False

for i in num:
    if (i < '0' or i > '9') and (i < 'a' or i > 'f'):
        error = True

while error == True:
    print('el valor hexadecimal introducido es incorrecto.')
    num = input('Introduzca un número hexadecimal: ')

    error = False

    for i in num:
        if (i < '0' or i > '9') and (i < 'a' or i > 'f'):
            error = True

print('El valor decimal del número {0} es {1}'.format(num, int(num, 16)))

