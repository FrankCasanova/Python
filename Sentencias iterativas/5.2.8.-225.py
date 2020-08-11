# programa que elimine de una listas todos los elementod de un valor par y
# muestre por pantalla el resultado.

lista = [1,-2,1,-5,0,3]

lista = [i for i in lista if i%2 == 0] 

print(lista) 