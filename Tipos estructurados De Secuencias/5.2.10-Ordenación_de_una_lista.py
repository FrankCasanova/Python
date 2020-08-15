lista =  ['Pepe', 'Juan', 'María', 'Ana', 'Luis', 'Pedro'] #[2,26,4,3,1]

for i in range(1, len(lista)):
    print('Pasada...\n', i) # Bucle que hace len(lista)-1 pasadas.
    for j in range(0, len(lista)-i):
        print(f'Comparación de lista {[j]} y lista {[j+1]}')

        if lista[j] > lista[j+1]:
            elemento = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = elemento
            print('Se intercambian')
        print(f'Estado actual de la lista es {lista}')






print(lista)
