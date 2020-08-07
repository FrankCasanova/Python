#diseñar un programa que muestre los n primeros números primos de un total de 100

totalPrim = 100

n = 7

lista = []

for num in range(2, totalPrim+1):

    primo = True

    for divisor in range(2, num):

        if num % divisor == 0:
            primo = False
            break
        else:
            if len(lista) <= n:
                
                lista.append(num)
                break 
print(lista)                





    

