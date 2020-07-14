# programa que dado na frase, un índice y un número, muestre una subfrase de la frase formada
# por el número de caracteres que empienzan en la posición del índice.


frase = 'Esternocleidomástoideo'  # input('Frase: ')

n = 8  # int(input('Dame un número: '))

i = 1  # int(input('Ahora un índice: '))

subFrase = ''

if n > len(frase):
    print('El número no puede ser mayor que la longitud de la frase.')
if i > len(frase) or i < 0:
    print('el indice introducido es incorrecto.')

for k in range(i, n):
    if i <= n:
        subFrase += frase[k]
    n += 1

print(subFrase)
