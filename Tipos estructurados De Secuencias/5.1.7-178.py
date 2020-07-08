# programa que convierte números de cualquier indole a decimal

num = input('intruduce un número: ')

num = num.lower()

hexadecimal = False
octal = False

for i in range(len(num)):
    if num[0] == '0' and num[1] == 'x':
        hexadecimal = True
    if num[0] == '0' and num[1] == 'o':
        octal = True

if hexadecimal:
    print('el número {0} en decimal sería {1}'.format(num, int(num, 16)))

elif octal:
    print('el número {0} en decimal sería {1}'.format(num, int(num, 8)))

else:
    print('el número es: ', num)
