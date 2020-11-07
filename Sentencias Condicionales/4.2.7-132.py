# programa para saber si un número es primo

num = int(input('Número: '))

if num > 1:
    primo = True
    for i in range(2, int(num/2)):
        if num % i == 0:
            primo = False
            break
else:
    primo = False

if primo:
    print('El número {0} es primo'.format(num))
else:
    print('El número {0} no es primo'.format(num))
