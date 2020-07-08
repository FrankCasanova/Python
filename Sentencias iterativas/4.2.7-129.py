# programa para saber el MCD de 2 números positivos.

num1 = int(input('Primer número: '))
num2 = int(input('Segundo número: '))

maxi = max(num1, num2)
mini = min(num1, num2)

mcd = False
i = mini
while not mcd and mini >= 1:
    if mini % i == 0 and maxi % i == 0:
        mcd = True
        print(i)
    else:
        i -= 1
