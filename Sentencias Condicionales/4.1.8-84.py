#PROGRAMA QUE CALCULE LA CANTIDAD DE AÑOS QUE SE TARDA EN CONSEGUIR UN CAPITAL FINAL.

from math import log

capital = float(input('Capital inicial: '))
taxes = float(input('Tasas de interes: '))
capitalFinal = float(input('Capital final: '))

if taxes != 0: 
    años = (log(capitalFinal) - log(capital)) / log(1+(taxes/100))
else:
    print('La tasa de interes no puede ser 0')    

print(años)