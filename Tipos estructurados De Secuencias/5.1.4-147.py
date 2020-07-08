# programa que calcule la letra del dni.

dni = int(input('Por favor indíqueme su DNI: '))

calc = dni % 23

letras = 'TRWAGMYFPDXBNJZSQVHLCKE'

letra = letras[calc]


print('Según los números de su DNI {0}, le corresponde la letra {1}, y quedaría tal que así: {0}{1}'.format(
    dni, letra,))
