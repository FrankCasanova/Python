# desing a function that returns a list with the perfect numbers between 1 and n.
# where n is an integer provided by the user.

def is_perfect(n):

    perfects = []

    for i in range(1, n + 1):

        plus = 0

        for j in range(1, i):

            if i % 2 != 0:
                continue

            if i % j == 0:
                plus += j

        if plus == i:
            perfects.append(plus)
            plus == 0
        else:
            plus == 0

    return perfects


number = int(input('plase, enter the number: \n\n >>> '))


print(is_perfect(number))
