#PROGRAMA QUE DETERMINE CUAL ES EL NÚMERO MÁS CERCANO AL PRIMERO.

num1 = int(input('Primer número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Tercer número: '))
num4 = int(input('Cuarto número: '))
num5 = int(input('Quinto número: '))

if num1 > num2:
    distancia1 = num1 - num2
else:
    distancia1 = num2 - num1
if num1 > num3:
    distancia2 = num1 - num3
else:
    distancia2 = num3 - num1   
if num1 > num4:
    distancia3 = num1 - num4
else:
    distancia3 = num4 - num1
if num1 > num5:
    distancia4 = num1 - num5
else:
    distancia4 = num5 - num1

if distancia1 < distancia2 and distancia1 < distancia3 and distancia1 < distancia4:
    candidato = num2
if distancia2 < distancia1 and distancia2 < distancia3 and distancia2 < distancia4:
    candidato = num3
if distancia3 < distancia1 and distancia3 < distancia2 and distancia3 < distancia4:
    candidato = num4
if distancia4 < distancia1 and distancia4 < distancia2 and distancia4 < distancia3:
    candidato = num5                    

print('El número más cercano a {0} es el número {1}'.format(num1, candidato))                               

