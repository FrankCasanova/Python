# programa que lea una cadea y muestre por pantalla una lista con todas 
# sus palabras en minúsculas. la lista devuelta no debe contener palabras repetidas.

frase ='Una frase formada con palabras,  otra frase con otras palabras.' #input('Introduzca una frase: \n')

frase = frase.lower()
frase = frase.replace(',', '')
frase = frase.replace('.', '')

frase = frase.split()

lista = []

[lista.append(i) for i in frase if i not in lista]

print(lista)

