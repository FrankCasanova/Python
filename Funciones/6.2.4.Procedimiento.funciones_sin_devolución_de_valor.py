# u can read this lesson on the book.

from time import time

tic = time()


def is_perfect(n):  # find out if the number n is perfect or not.
    sumatorio = 0
    for i in range(1, n):
        if n % i == 0:
            sumatorio += i
    return sumatorio == n


def perfects_table(m):  # show all perfect numbers between 1 and m.
    for i in range(1, m + 1):
        if is_perfect(i):
            print(i, 'is a perfect number')


number = 10000  # int(input('Give me a number: \n'))
perfects_table(number)

toc = time()
print(toc - tic)
