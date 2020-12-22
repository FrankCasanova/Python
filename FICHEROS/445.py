# make a function that, given the path of a file and a word, returns a
# list witn the lines that contain that word
# then design a program that reads the name of a file and as many words as the user
# wants (uses a loop that asks the user
# if they want to continue entering words)
# for each word, the program will show the lines that contain that word in the
# file


def word_in_file(aList, files):
    """
    return a list with the lines 
    that contain a list of given words
   """
    
#%%    
    with open(files, 'r') as file:

        for index, line in enumerate(file):
            for word in aList:
                if word in line:
                    print(f'La palabra {word} aparece en la línea {index}')

#%%
file_name = 'Bio.txt'
words = ['Bueno', 'batería']

word_in_file(words, file_name)
