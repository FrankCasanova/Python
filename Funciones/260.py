# the last letter of the id can be calculated from the number.
# for them you just have to divide the number by 23 and keep the rest,
# which is a number between 0 and 22.
# the letter that corresponds to echa number is found in this table (book theme 6)

def id_letter(x):

    listLetters = 'TRWAGMYFPDXBNJZSQVHLCKE'

    letter = x % 23

    return listLetters[letter]


print(id_letter(48952877))
