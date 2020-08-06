#ejercicio que asigna dos listas a 2 variables y nos diga si la primera lista es menor que la segunda.
#no está permitido usar las comparaciones.

lista1, lista2 = [1,2,3,4,], [1,2,3]

if len(lista1) < len(lista2):

    print(f'la primera lista es más corta que la segunda')

else:
    print(f'la primera lista NO es más corta que la segunda')