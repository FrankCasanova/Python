# improve the is_perfect function by making it faster.
# is it really necessary to consider all numbers between 1 and n-1?


def is_perfect(n):

    plus = 0

    for i in range(1, n):

        if n % 2 != 0:
            print(n, 'no es un número par')
            break

        if n % i == 0:

            plus += i

    return plus == n


print(is_perfect(8128))
