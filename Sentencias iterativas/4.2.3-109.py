#PROGRAMA QUE PIDA AL USUARIO UN NÚMERO ENTRE 1 Y 10 AMBOS INCLUSIVE 

num = float(input('Introduzca un número entre 1 y 10: '))

while num < 1 or num > 10:
    print('valor incorrecto. ')
    num = float(input('Introduzca un número entre 1 y 10: '))

print(num)    

