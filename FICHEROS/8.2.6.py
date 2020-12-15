# file_name = input('File: ')
# new_line = input('Line: ')

# copy_name = file_name + '.copy'

# #we make the copy
# with open(file_name, 'r') as file1, open(copy_name, 'w') as file2:

#     [file2.write(line) for line in file1]

# # and we remake the original by adding the new line

# with open(copy_name, 'r') as file1, open(file_name, 'w') as file2:

#     [file2.write(line) for line in file1]
#     file2.write(new_line + '\n')
#     pass

grade = int(input('Exam Grade: '))

with open('notas.txt', 'a') as file:

    file.write(str(grade) + '\n')
