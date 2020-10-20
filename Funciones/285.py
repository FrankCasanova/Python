
# make a function that receives a DNI
# number and a letter. the function will
# return Trur if the letter corresponds to
# that DNI number, and false otherwise
# The function must be called, dni_check


def dni_check(number, lett):

    if lett == letter_to_check:
        return True

    else:
        return False


def id_letter(x):

    listLetters = 'TRWAGMYFPDXBNJZSQVHLCKE'

    letter = x % 23

    letter = str(listLetters[letter])

    return letter


dni_number = 48952877
dni_letter = 'T'

print('bienvenido al programa de checkeo de DNI')
print('vamos a comprobar si su DNI es verdadero')
print(f'su número de DNI es {dni_number}')
print(f'su letra de DNI es {dni_letter}')

letter_to_check = id_letter(dni_number)
dni_check(dni_number, dni_letter)

if dni_check == True:
    print('su DNI es verdadero')
else:
    print('vaya, parece que su DNI es falso')
