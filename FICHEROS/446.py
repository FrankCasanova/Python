# make a programa that shows the longest
# line of a file, if there is more than one line
# with the length of the longest, the program will only show the
# first of them.
# (the name of the file will be requested from the user by keyboard)

file_name = 'Bio.txt'

with open(file_name, 'r') as file:

    largest = 0
    line_large = ''

    for index, line in enumerate(file):
        if len(line) > largest:
            largest = len(line)
            line_large = line


print(
    f'La línea más larga es la línea {largest}\ncon la frase:\n{line_large}')
