# desings a function that, given a list of strings, return the longest string.
# if two or more  have the same length and are the lonfest, the function will
# return any one of them

def largest_str(string):

    largest = None

    for index, snts in enumerate(string):

        if largest == None:
            largest = snts

        if len(snts) > len(largest):
            largest = string[index]

    return largest


list_strings = ['hola que pasa', 'hoy no quiero salir de mi casa la verdad',
                'no sé por qué no me he quedado en casa']


print(largest_str(list_strings))
