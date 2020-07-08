#PROGRAMA QUE VAYA LEYENDO NÚMEROS Y MOSTRÁNDOLOS POR PANTALLA HASTA QUE EL USUARIO MUESTRE UN NÚMERO NEGATIVO.

num = int(input('Número: '))

while num >= 0:
    print(num)
    num = int(input('Número: '))

print('Gracias por usar nuestro servicio.')    