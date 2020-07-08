# maximo comun divisor de 3 números.

num1 = int(input('Primer número:'))
num2 = int(input('Segundo número:'))
num3 = int(input('Tercero número:'))

maxi = max(num1, num2, num3)
mini = min(num1, num2, num3)

if num1 != maxi and num1 != mini:
    medi = num1
if num2 != maxi and num2 != mini:
    medi = num2
if num3 != maxi and num3 != mini:
    medi = num2

mcd = False
i = mini
while not mcd and mini >= 1:
    if mini % i == 0 and medi % i == 0 and maxi % i == 0:
        mcd = True
        print(i)
    else:
        i -= 1
