# programa de desglose de dinero

dinero = int(input('Cantidad de dinero a desglosar: '))

print('desglose en billetes de una cantidad de {0} euros.'.format(dinero))

for desglose in [500, 200, 100, 50, 20, 10, 5, 2, 1]:
    billetes = dinero // desglose
    dinero = dinero - (billetes*desglose)
    if billetes > 0 and (desglose != 2 or desglose != 1):
        if billetes > 1:
            print('{0} billetes de {1} euros'.format(billetes, desglose))
        else:
            print('{0} billete de {1} euro'.format(billetes, desglose))

    if billetes > 0 and (desglose == 2 or desglose == 1):
        if billetes > 1:
            print('{0} monedas de {1} euros'.format(billetes, desglose))
        else:
            print('{0} moneda de {1} euro'.format(billetes, desglose))
