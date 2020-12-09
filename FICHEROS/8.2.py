
input = open('Bio.txt', 'r')
output = open('Bio.txt', 'w')

carácter = input.read(1):

while carácter != '':
    if carácter >= 'a' and carácter <= 'y':
        code = chr(ord(carácter)+1)
    elif carácter == 'z':
        code = 'a'
    else:
        code = carácter
    carácter = input.read(1)
    
input.close()
output.close()


