# ejemplo

limit = int(input('Dame un número: '))

for num in range(2, limit):
    primo = True
    for divisor in range(2, num):
        if num % divisor == 0:
            primo = False
            break
    if primo:
        print('el número {0} es primo'.format(num))
