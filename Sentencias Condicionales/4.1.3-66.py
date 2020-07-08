#programa que calcule el desglose mínimo en billetes y monedas de euro.

dinero = int(input('Introduzca cuanto dinero quiere desglosar: '))

billetes500 = dinero // 500

if billetes500 > 0:

    print('{0} billete(s) de 500 euros.'.format(billetes500))

    dinero = dinero - (billetes500*500)    

billetes200 = dinero // 200

if billetes200 > 0:

    print('{0} billete(s) de 200 euros.'.format(billetes200))

    dinero = dinero - (billetes200*200)

billetes100 = dinero // 100

if billetes100 > 0:

    print('{0} billete(s) de 100 euros.'.format(billetes100))

    dinero = dinero - (billetes100*100)

billetes50 = dinero // 50

if billetes50 > 0:

    print('{0} billete(s) de 50.'.format(billetes50))

    dinero = dinero - (billetes50*50)    

billetes20 = dinero // 20

if billetes20 > 0:

    print('{0} billete(s) de 20.'.format(billetes20))

    dinero = dinero - (billetes20*20)

billetes10 = dinero // 10

if billetes10 > 0:

    print('{0} billete(s) de 10 euros.'.format(billetes10))

    dinero = dinero - (billetes10*10) 

billetes5 = dinero // 5

if billetes5 > 0:

    print('{0} billete(s) de 5 euros.'.format(billetes5))

    dinero = dinero - (billetes5*5) 

moneda2 = dinero // 2

if moneda2 > 0:

    print('{0} moneda(s) de 2 euros.'.format(moneda2))

    dinero = dinero - (moneda2*2)

if dinero == 1:

    print('y una moneda de un éuro.')     

