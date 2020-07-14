# programa que lea 2 palabras y diga si una subpalabra está dentro de la palabra.

palabra1, palabra2 = 'subcadena', 'sub'
sub = False
for i in range(len(palabra1)):
    if palabra2 in palabra1[i: i+len(palabra2)]:
        sub = True
        break


print(sub)
