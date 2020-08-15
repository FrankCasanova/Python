# En una cadena llamada texto disponemos de un texto formado por varias frases.
# Escribe un programa que determine y demuestre el número de palabras de cada frase.

frase = 'Esto es una frase más o menos corta. Y esto es otra frase, normalita, no tiene nada especial.'

sepFrase = frase.split('.') 
sepFrase.pop()

palabrasFrase = [len(i) for i in sepFrase]

#for i in sepFrase :

print(palabrasFrase)
