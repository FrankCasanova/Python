# programa que muestre la tabla de multiplicar.

num = int(input('Dame un número: '))

for multiplicar in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print('{0} x {1} = {2}'.format(num, multiplicar, num*multiplicar))
