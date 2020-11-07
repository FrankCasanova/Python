# desing a duplicate_copy function that
# receives a list of numbers and returns another list
# in which each element is twice
# the one with the same index in the original.
# the original list should not undergo any modification
# after the duplicate_copy call

import doctest


def duplicate_copy(a_list):
    """
    returns a list with each element
    duplicate.
    >>> duplicate_copy([2,3,4])
    [4, 6, 8]
    """
    doubling = [it*2 for it in a_list]

    return doubling


my_list = [3, 5, 4, 7, 6, 2, 8, ]


print(my_list)
print(duplicate_copy(my_list))
