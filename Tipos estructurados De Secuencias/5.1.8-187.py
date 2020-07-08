# programa que sume 2 números binarios.

bi1 = input('Primer número binario: ')
bi2 = input('Segúndo número binario: ')
checkbi1 = True
checkbi2 = True


for i in bi1:
    if i != '0' and i != '1':
        checkbi1 = False
        break

if checkbi1:
    for i in bi2:
        if i != '0' and i != '1':
            checkbi2 = False
            break


if checkbi1 and checkbi2:
    suma = bin(int(bi1)) + bin(int(bi2))
    print(suma)
else:
    print('algunos de los números indicados no es binario')
