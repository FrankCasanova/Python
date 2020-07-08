# programa de sumatorio n y m i2.

n = int(input('Indiqueme el valor de n: '))
m = int(input('Indiqume el valor de m: '))
resultado = 0
for i in range(n, m+1,):
    resultado = i**2
    print(resultado)
