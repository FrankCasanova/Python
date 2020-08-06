
try:

    while (final := int(input('Por favor, indique el valor final de la lista:   \n (presiona una tecla que no sea númerica para salir.\n número: '))) and isinstance(final,int):
        
        
            a = list(range(1,final))

            a = [i*i for i in range(len(a))]

            print(a)

except ValueError:
    print('gracias por usar nuestro servicio')            
        



