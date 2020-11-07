# desin a duplicate function that receives a list of numbers
# and modifies it by
# doubling the value of each of its
# elements.

import numpy as np


def duplicate(a_list):
    """
    modify a list doubling each value in it

    """
    for it, num in enumerate(a_list):
        aux = num*2
        a_list[it] = aux


rlist = [1, 2, 3]
duplicate(rlist)

print(rlist)
