# Words Count

contador = {}

print('Ve introduciendo líneas (línea vacía para acabar)')
línea = input('Línea: ')

while línea != '':

    palabras = línea.split()
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    línea = input('Línea: ')

# we get the list of different words

palabras = list(contador.items())

# we order the list of words

palabras.sort()

# recorremos la lista ordenada para ostrar cada contador

print('Se han encontrado las siguientes palabras: ')
for palabra in palabras:
    print(palabra)
