# programa que indique si una frase tiene dígitos o no, y los muestre.

frase = input('escriba su frase, puede incluir números: ')

while frase != '':

    lista = []
    contador = 0

    for i in frase:
        if i >= '0' and i <= '9':
            contador += 1
            lista.append(i)
    break

print('Existen {0} dígitos, los cuales son: '.format(contador))

for i in range(len(lista)):
    if i == len(lista)-1:
        print('y el', lista[i])
        break
    print('el', lista[i])
