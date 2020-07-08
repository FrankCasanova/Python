# Programa que lea una frase y diga si contiene digito o si no contiene digito.

frase = input('Escriba la frase a analizar: ')

cont_digit = False

for i in frase:
    if i >= '0' and i <= '9':
        cont_digit = True

if not cont_digit:
    print('La frase no contiene dígitos.')
else:
    print('La frase contiene dígitos.')
