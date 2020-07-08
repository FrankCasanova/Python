#programa que compara edades y dice cual de las personas es la más joven o si tienen la misma edad.

edad1 = int(input('Edad del primer individuo: '))
edad2 = int(input('Edad del segundo individuo: '))

if edad1 == edad2:

    print('ambos individuos tienen la misma edad. ')


if edad1 > edad2:

    print('El segundo individuo es más jóven.')

else:

    print('El primer individuo es más jóven. ')

    