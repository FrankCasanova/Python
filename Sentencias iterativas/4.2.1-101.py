#programa que muestre todos los multiplos de n entre n y m.

número = int(input('Número: '))
máximo = int(input('Máximo: '))

i = número


while i <= máximo:
    if i % número == 0:
        print(i)
        i +=1
    else:
        i +=1    