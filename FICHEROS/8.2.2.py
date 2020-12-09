
# step one: open file.

# with open('Bio.txt', 'r') as file:

# step two: read data from file.

#[print(line) for line in file]

# for line in file:
#     if line[-1] == '\n':
#         line = line[:-1]
#     print(line)

name = input('File name: ')

with open(name) as file:

    count = len([i for i, o in enumerate(file)])


print(count)
