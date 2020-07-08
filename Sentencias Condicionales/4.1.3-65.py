# programa que muestre si el segúndo número es el cuadrado del primero.
# o si el segundo número es menor que el cuadrado del primero.
# o si el segundo número es mayor que el cuadrado del primero

num1 = int(input('Introduzca el primer número: '))
num2 = int(input('Introduzca el segúndo número: '))

if (num1 ** 2) == num2:

    print('El segúndo número es el cuadrado del primero.')

elif (num1 ** 2) < num2:

    print('El segúndo número es mayor que el cuadrado del primero. ')


else:

    print('El segúndo número es menor que el cuadrado del primero.')