#MÁXIMO DE 3 NÚMEROS.

a = int(input('El primer número: '))
b = int(input('El segundo número: '))
c = int(input('El tercer número: '))

if a > b:
    if a > c:
        máximo = a
    else:
        máximo = c
else:
    if b > c:
        máximo = b
    else:
        máximo = c

print('El máximo es', máximo)                        