
file_name = input('File name: ')

with open(file_name, 'r') as file:

    count = 0
    character = file.read(1)

    while character != '':
        count += 1
        character = file.read(1)

print(count)
