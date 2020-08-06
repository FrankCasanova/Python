# programa que lea 3 palabras y muestre el prefijo más largo común en las 3.

palabra1, palabra2, palabra3 = 'politécnico', 'polinización', 'polimorfos'

sub = ''

for i in range(len(palabra1)):
    if palabra1[i] == palabra2[i] == palabra3[i]:
        sub += palabra1[i]
    else:
        break

print(sub)
