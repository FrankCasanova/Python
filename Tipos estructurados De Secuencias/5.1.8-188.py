# prgrama de encriptacion

frase ='wyz' #input('Escriba la frase que desea encriptar: ')

frase = frase.lower()

crip1 = []

for i in frase:

    if i == 'z':
        crip1.append(ord('b'))
    elif i == 'y':
        crip1.append(ord('a'))
    else:     
        crip1.append(ord(i) + 2)

crip2 = []


for i in crip1:
    crip2.append(chr(i))


print(''.join(crip2))
    