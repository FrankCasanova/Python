# programa comprobador de binarios.

#binary = input('introduzca su código binario: ')
correcto = False

while not correcto:

    if not correcto:
        binary = input('introduzca su código binario: ')

    for i in range(len(binary)):

        if binary[i] == '1' or binary[i] == '0':
            correcto = True
        else:
            correcto = False
            print('Un código binario solo puede contener 1 y 0.')
            break

print('El código introducido es correcto')
