#modificación del ejercicio 104

sumatorio = int(input('Sumatorio: '))
limit = int(input('Número límite: '))

i = 1

while sumatorio > limit:
    print('El sumatorio no puede ser superior al límite.')

    sumatorio = int(input('Sumatorio: '))
    limit = int(input('Número límite: '))

    i = 1

while i <= limit:
    sumatorio += i 
    i +=1

print(sumatorio)    


    
    