# AMPLIACIÓN DEL PROGRAMA DE DETECCIÓN DE LETRAS.

letra = str(input('Letra: '))

if letra >= 'a' and letra <= 'z' or letra == 'ñ':
    print('Es una minúsucula')

elif letra >= 'A' and letra <= 'Z' or letra == 'Ñ':
    print('Es una mayúscula.')

else:
    print('No es una letra.')
