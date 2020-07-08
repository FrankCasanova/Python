#PROGRAMA DE DETECCIÓN DE VOCALES O CONSONANTES MAYUSCULAS O MINÚSCULAS.

letra = input('ingresa la letra: ')

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('{0} es una vocal minúsucula.'.format(letra))
else: 
    if letra >= 'b' and letra < 'z':
        print('{0} es una consonante minúscula.'.format(letra)) 

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('{0} es una vocal mayúscula.'.format(letra))

else:
    if letra >= 'B' and letra < 'Z':
        print('{0} es una consonante mayúsucula.'.format(letra))
