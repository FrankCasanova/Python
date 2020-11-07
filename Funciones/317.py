# desing a function that, given a list of numbers, returns a list
# with all the pairs of friendly numbers that we can form with
# one from the firs list and oanother from the second list
import doctest


def is_perfect(n):
    '''
    check if the numer is perfect or not.

    >>> is_perfect(28)
    True

    '''

    sumatorio = int(sum([i for i in range(1, n) if n % i == 0]))

    # for i in range(1, n):
    #     if n % i == 0:
    #         sumatorio += i

    return sumatorio == n


list_num = [45, 34, 2, 3, 43, 2, 6, 68, 26, 34, 496, 23, 4, 5]
print(is_perfect(28))

doctest.testmod()
