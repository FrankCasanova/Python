#Programa para calcular el número de convinaciones posibles.

trabajadores = int(input('Indique el número de trabajadores: '))
puestosDeTrabajo = int(input('Indique número de puestos de trabajo: '))

facTrabajadores = 1
facNumPuestos = 1

i = 1

while i <= trabajadores:
    facTrabajadores *= i
    i += 1

i = 1

while i <= puestosDeTrabajo:
    facNumPuestos *= i
    i += 1    

i = 1

factoTrabPuestos = 1

while i <= (trabajadores - puestosDeTrabajo):
    factoTrabPuestos *= i
    i += 1

combinaciones = facTrabajadores / (facNumPuestos*factoTrabPuestos)

print(combinaciones)




