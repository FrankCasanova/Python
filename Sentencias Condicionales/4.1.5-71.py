#PROGRAMA DE DETECCIÓN DE LETRA MAYÚSCULA O MINÚSCULA AMPLIADO.

letra = str(input('Letra: '))

if letra <= 'a' and letra >= 'z':
    print('Es minúscula')

elif letra >= 'A' and letra <= 'Z':
    print('Es mayúscula')

else:
    print('No es una letra.')    
