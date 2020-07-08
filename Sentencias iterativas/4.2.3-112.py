#PROGRAMA QUE VAYA REGISTRANDO NÚMERO Y AL TECLEAR UNO NEGATIVO MUESTRE EL MAYOR DE LOS INTRODUCIDOS

num = int(input('Número: '))
mayor = 0

while num >= 0:
    print(num)
    if mayor < num:
        mayor = num
    num = int(input('Número: '))

print(mayor)        

