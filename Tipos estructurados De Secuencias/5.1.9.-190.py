# programa de subcadenas.

frase = 'ejemplo'  # input('Frase: ')
i = -5  # int(input('Dame un número: '))
j = 20  # int(input('Dame otro número: '))

if j > len(frase):
    final = len(frase)
else:
    final = j
if i < 0:
    principio = len(frase)-len(frase)
else:
    principio = i

subFrase = ''

for k in range(principio, final):
    subFrase += frase[k]

print(subFrase)
