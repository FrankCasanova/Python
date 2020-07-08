#programa que muestre la raiz n-sima de un número mostrado por teclado.

num = int(input('Número: '))

for n in range(2,101):
    print('la raiz {0}-esima de {1} es {2}'.format(n,num,num**(1/n)))