# programa que diga si un número es entero o no.

num = input('Número: ')

while num != '':

    entero = False

    for i in range(len(num)):

        if num[i] >= '0' and num[i] <= '9':

            entero = True

        else:
            entero = False
            break

    if entero:
        print('Es un número entero.')
        break
    else:
        print('No es un número entero.')
        break
