#Programa que pida el lado de un cuadrado y muestre su perímetro y área.

#datos

lado = float(input('Valor del lado: '))

#fórmula

perímetro = lado*4
área = lado*lado

print('El perímetro es de {0} metros, y el área de {1}'.format(perímetro, área))
