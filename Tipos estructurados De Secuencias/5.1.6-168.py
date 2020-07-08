# programacomprobador de floats.

num = '3.1e-2'

while num != '':

    tieneNumero = False
    tienePunto = False

    contadorPunto = 0
    contadorOperador = 0
    contadorE = 0

    for i in range(len(num)):
        if num[i] <= '9' and num[i] >= '0':
            tieneNumero = True
        else:
            if num[i] != 'e' and num[i] != 'E' and num[i] != '.' and num[i] != '+' and num[i] != '-':
                tieneNumero = False
                break

        if num[i] == 'e' or num[i] == 'E' or num[i] == '.' or num[i] == '+' or num[i] == '-':
            if num[i] == '.':
                contadorPunto += 1
            if num[i] == 'e' or num[i] == 'E':
                contadorE += 1
            if num[i] == '+' or num[i] == '-':
                contadorOperador += 1

            tienePunto = True

        if num[i] == '.' and num[i] == num[len(num) - 1]:
            tieneNumero = False
            break

    if tienePunto and tieneNumero and contadorPunto == 1 and contadorOperador < 2 and contadorE < 2:
        print('El número indicado es un flotante.')
        break
    else:
        print('El número indicado NO es un flotante')
        break
