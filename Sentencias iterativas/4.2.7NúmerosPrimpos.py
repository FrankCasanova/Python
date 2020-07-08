# número = 7

# for divisor in range (2, número):
#    print('{0} entre {1} '.format(número, divisor), end='')
#    print('es {0} con resto {1}'.format(número // divisor, número % divisor))

# restoNoNulo = 0
# for divisor in range(2, número):
#    if número % divisor != 0:
#        restoNoNulo += 1

# if restoNoNulo == número - 2:
#     print('El número {0} es primo.'.format(número))
# else:
#    print('El número {0} no es un número primo'.format(número))

# primo = True
# for divisor in range(2, número):
#    if número % divisor == 0:
#        primo = False

# if primo:
#    print('El número {0} es primo'.format(número))
# else:
#    print('El número {0} no primo'.format(número))

# num = int(input('Número: '))

# if num > 1:
#    verificador = True

#    for i in range(2, num):
#        if num % i == 0:
#        verificador = False
# else:
#    verificador = False

# if True:
#    print('El número {0} es primo'.format(num))
# else:
#    print('El número {0} no es primo'.format(num))

num = int(input('Número a evaluar: '))

if num > 1:
    verificador = True
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            verificador = False
        divisor += 1
else:
    verificador = False

if verificador:
    print('El número {0} es primo'.format(num))
else:
    print('El número {0} no es primo'.format(num))
