# desing a function that receives a list and returns another list
# whose content is the result of concatenating the original list
# with itsel. the original list should not be modified

import doctest


def concatenating(a_list):
    """
    returns another list whose content is the
    result of concatenating the original list
    with itself
    >>> concatenating([1, 2, 3])
    [1, 2, 3, 1, 2, 3]
    """
    concate = a_list + a_list

    return concate


my_list = [2, 3, 4]

print(concatenating(my_list))
