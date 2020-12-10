# make a program that, given the name of
# a file, displays each of its lines preceded by
# its line number. (the name of the file will be requested
# from the user by keyboard)

name_file = 'Bio.txt'

with open(name_file, 'r') as file:
    number = 1

    for index, line in enumerate(file):

        print(line.strip(), index)
