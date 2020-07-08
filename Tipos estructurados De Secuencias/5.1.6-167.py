# programa de verificador de variables.

identificación = input('Ingrese su identificador: ')

validación = True

for i in identificación:
    if i >= '0' and i <= '9':
        validación = False

if validación:
    print('Validación correcta.')
else:
    print('Validación incorrecta.')

