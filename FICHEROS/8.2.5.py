# input_name = 'Bio.txt'
# output_name = 'code_bio.txt'
# input_file = open(input_name, 'r')
# output_file = open(output_name, 'w')

# character = input_file.read(1)

# while character != '':
#     if character >= 'a' and character <= 'y':
#         code = chr(ord(character)+1)
#     elif character == 'z':
#         code = 'a'
#     else:
#         code = character

#     output_file.write(code)
#     character = input_file.read(1)

# input_file.close()
# output_file.close()


input_name = 'Bio.txt'
output_name = 'code_bio.txt'

with open(input_name, 'r') as input_file, open(output_name, 'w') as output_file:

    for line in input_file:
        new_line = ''
        for character in line:
            if character >= 'a' and character <= 'y':
                code_line = chr(ord(character)+1)
            elif character == 'z':
                code_line = 'a'
            else:
                code_line = character
                new_line += code_line
                output_file.write(new_line)
