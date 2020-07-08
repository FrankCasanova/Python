#programa que calcule sumatorios de n y m 

sumatorio = int(input('sumatorio: '))
limit = int(input('Límite máximo: '))

i = 1

while i <= limit:
    sumatorio += i
    i +=1

print(sumatorio)    