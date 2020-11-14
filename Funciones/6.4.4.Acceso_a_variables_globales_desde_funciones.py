# book example.

carga50 = 100
carga20 = 100
carga10 = 100


def sacar_dinero(cantidad):

    global carga50, carga20, carga10

    if cantidad <= 50*carga50 + 20*carga20 + 10*carga10:

        de50 = cantidad // 50
        cantidad = cantidad % 50
        if de50 >= carga50:  # si no hay suficientes billetes de 50
            cantidad = cantidad + (de50 - carga50)*50
            de50 = carga50

        de20 = cantidad // 20
        cantidad = cantidad % 20
        if de20 >= carga20:  # si no hay suficientes billetes de 20
            cantidad = cantidad + (de20 - carga20)*20
            de20 = carga20

        de10 = cantidad // 10
        cantidad = cantidad % 10
        if de10 >= carga10:  # si no hay suficientes billetes de 10
            cantidad = cantidad + (de10 - carga10)*10
            de10 = carga10
        # si todo ha ido bien, la cantidad que resta por entregar es nula
        if cantidad == 0:
            carga50 = carga50 - de50
            carga20 = carga20 - de20
            carga10 = carga10 - de10
            return [de50, de20, de10]
        else:  # y sino, devolvemos la lista con tres ceros:
            return[0, 0, 0]

    else:
        return[0, 0, 0]


# PROGRAMA PRINCIPAL
while 50*carga50 + 20*carga20 + 10*carga10 > 0:

    peticion = int(input('Cantidad que desea sacar: '))

    [de50, de20, de10] = sacar_dinero(peticion)

    if [de50, de20, de10] != [0, 0, 0]:
        if de50 > 0:
            print(f'Billetes de 50 euros {de50}')
        if de20 > 0:
            print(f'Billetes de 20 euros {de20}')
        if de10 > 0:
            print(f'Billetes de 10 euros {de10}')

        print('Gracias por usar el cajero.\n')

    else:
        print('Lamento no poder atender su petición.\n')

print('Cajero sin dinero, avise a mantenimiento.')
