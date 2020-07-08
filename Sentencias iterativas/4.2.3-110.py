#PROGRAMA QUE RECHACE LETRAS MAYUSCULAS.

text = input('introduzca un texto que no contenga letras mayusculas: ')

while text.lower() != text: 

    print('El texto no puede contener mayúsculas.')
    text = input('introduzca un texto que no contenga letras mayusculas: ')

print(text)