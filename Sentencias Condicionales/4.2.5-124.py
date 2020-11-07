# caluclo de sumatorias entre n y m solo de los números pares.

n = int(input('Valor de n: '))
m = int(input('Valor de m: '))
sumatorio = 0
for i in range(n, m+1, 2):
    sumatorio += i
    print(sumatorio)
