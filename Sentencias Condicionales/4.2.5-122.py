#programa que pida el valor de 2 enteros y muestre por pantalla el sumatorio

num = int(input('Inicio del sumatorio: '))
final = int(input('cantidad de operaciones: '))

resultado = 0
for i in range(num,final):
    resultado += i
    print(resultado)

