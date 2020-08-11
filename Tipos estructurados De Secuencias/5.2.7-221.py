# programa que lea una lista de 10 enteros, pero asegurándose de que
# todos los números introducidos pr el usuario son positivos. cuando el número sea negativo,
# lo indicaremos con un mensaje y permitiremos al usuario repetir el intento cuantas veces sea preciso.

lista = []
try:
    while (num := int(input('Número: \n'))) and len(lista) < 10:

        if num > 0:

            lista.append(num)

        else:
            print('El número no puede ser negativo.') 


except ValueError: print('El valor tiene que ser un número.')


       

print(lista)       








