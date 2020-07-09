# programa para desencriptar

frase = input('Escriba la frase que desea encriptar: ').lower()
abc = 'abcdefghijklmnñopqrstuvwxyz'
crip = ''
k = int(input('Valor de encriptación: '))


for i in frase:
    if i in abc:

        try:

            crip += abc[(abc.index(i) - k)]

        except IndexError:

            crip += abc[k + (abc.index(i))]

    else:
        crip += i


print('Su texto cifrado es: ', crip)
