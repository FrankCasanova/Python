import numpy as np


def factorial(n):
    """
    docstring
    """
    return int(np.prod([i for i in range(1, n+1)]))


def combinations(n, m):
    return round(factorial(n) / (factorial(n-m)*(factorial(m))), 2)


print(combinations(15, 7))
