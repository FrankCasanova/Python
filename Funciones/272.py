# desing a function that calculates the producer of all the numbers that make up a list.

import numpy as np


def producer(array):

    return np.prod(array)


a_list = [4, 5, 6, 44, 2, 43, 6, 3]

print(producer(a_list))
