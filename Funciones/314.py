# design a function that, given a list of names and a letter,
# returns a list of all the names beginning with that letter


def they_start_with(list1, letter):
    return [i for i in list1 if i[0] == letter]


names = ['josefa', 'pedro', 'marcos', 'miriam', 'enrique', 'sofián', 'maría']
letter = 'm'

print(they_start_with(names, letter))
