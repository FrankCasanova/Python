#de 5 palabras, cual es la menor según la tabla ASCII.

word1 = input('Primera palabra: ')
word2 = input('Segúnda palabra: ')
word3 = input('Tercera palabra: ')
word4 = input('Cuarta palabra: ')
word5 = input('Quinta palabra: ')

larga = word1

if word2 > larga:
    larga = word2
if word3 > larga:
    larga = word3
if word4 > larga:
    larga = word4        
if word5 > larga:
    larga = word5

print('La palabra más larga es', larga)    
 