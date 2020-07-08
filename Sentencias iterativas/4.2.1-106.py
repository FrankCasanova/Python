# programa de calculo de factorial de un número n.


try:
    num = int(input('Número que desea factorizar: '))

except ValueError:
    print('tiene que ser un número entero y positivo ')

while num < 0:
    print('El número tiene que ser positivo. (mayor que 0)')

    try:
        num = int(input('Número que desea factorizar: '))

    except ValueError:
        print('tiene que ser un número entero y positivo ')

i = 1
factorial = 1

while i <= num:
    factorial = factorial*i
    i +=1

    


print(factorial)

