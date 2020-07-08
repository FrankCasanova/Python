#programa de calificación de notas


nota = float(input('Cuál fue su calificación: '))

if nota < 5:
    print('Insuficiente.')

elif nota >= 5 and nota < 7:
    print('Aprobado.')

elif nota >= 7 and nota < 9:
    print('Notable')

elif nota >= 9 and nota < 10:
    print('Sobresaliente')

elif nota == 10:
    print('Matrícula')  

      
