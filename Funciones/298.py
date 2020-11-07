# design a function that receives a list of
# integers and returns the minimum and
# maximum numbers from the list
# simultaneously

import numpy as np


def minMax(l):

    mini = np.max(l)
    maxi = np.min(l)

    return [mini, maxi]


listNumber = [2, 54, 34, 67, 3434, 54545, 12, 2,
              4, 3, 43, 4, 34352, 454, 23, 4343, 2, 34, ]

print(minMax(listNumber))
