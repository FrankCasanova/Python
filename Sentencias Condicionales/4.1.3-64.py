#programa que indique si un número es el doble de un número impar

num = int(input('Introduzca número: '))

mitad = num / 2

if (mitad % 2) != 0:

    print('{0} es el doble de un número impar, el cual es {1}.'.format(num, mitad))

else:

    print('{0} no es el doble de un número impar, el cual es {1}.'.format(num, mitad))    