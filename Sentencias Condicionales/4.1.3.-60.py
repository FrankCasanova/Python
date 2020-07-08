#programa que lea si hay un parentesis abierto o cerrado.

caracter = input('teclée un carácter: ')

if caracter != '(' and caracter != ')':

    print('El carácter introducido no es parentesis')

if caracter == '(':

    print('El carácter introducido es un carácter de abrir parentesis.')

elif caracter == ')':

    print('El carácter introducido es un carácter de cerrar parentesis.')
    
           