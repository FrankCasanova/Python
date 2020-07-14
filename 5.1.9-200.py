# programa que lea 2 palabras y nos diga el prefijo común más largo.

palabra1, palabra2 = 'politécnico', 'politérmo'

sub = ''

for i in range(len(palabra1)):

    try:
        if palabra1[i] == palabra2[i]:
            sub += palabra1[i]
        else:
            break
    except IndexError:
        break
print(sub)
