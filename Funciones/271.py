# make a function that takes a listo of numbers and returns the mean of those numbers
# be careful with empty lists (their mean is zero)


import numpy as np


def median(array):

    return np.median(array)


a_list = [6, 45, 33, 4, 5, 76, 0, 12, 4, 4, 666, ]

print(median(a_list))
