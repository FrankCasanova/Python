# make a program that, given a word and a file name, says whether or not the word
# appears in the file, the file name and the
# word and will ask the user by keyboard.


file_name = input('File name: ')
word = input('Word: ')

with open(file_name, 'r') as file:

    exist = False

    for line in file:
        if word in line:
            exist = True
            break

if exist:
    print('Exist')
else:
    print('Does not exist')
