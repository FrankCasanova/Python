#TESTEO DE PROGRAMA

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

if a == 0 and b == 0 and c == 0:
    print('la ecuación tiene infinitas soluciones.')
else:
    if a == 0 and b == 0:
        print('La ecuación no tiene solución.')
    else:
        if a == 0:
            x = -c / b
            print('Solución: x={0:.3f}'.format(x))

        else: 
            x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
            x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
            print('Las soluciones son x1={0:.3} y x2={1:.3}'.format(x1,x2))            