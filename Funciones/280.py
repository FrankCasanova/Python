# defines a function that, given the
# parameters b and x, returns the value of
# logb(x) that is, the logarithm in base b of x

from math import log


def logarithm(x, b):
    return log(x, b)


print('el logaritmo de 7 en base 3 es:\n\n', logarithm(7, 3), '\n\n')
