# programa para descubrir si un número es primo. explorando hasta su raiz

from math import sqrt

num = int(input('Número: '))

if num < 1:
    primo = True
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            primo = False
            break
else:
    primo = False

if primo:
    print('El número {0} es primo'.format(num))
else:
    print('El número {0} no es primo'.format(num))
