
try:

    while (n := int(input('Deme un número: '))) and isinstance(n, int):

        numPrim = []

        for num in range(2, n+1):
            prim = True
            for divisor in range(2, num):
                if num % divisor == 0:
                    prim = False
                    break
            if prim:
                numPrim.append(num)
        print(numPrim)

except ValueError:
    print('Gracias por usar nuestro servicio.')

