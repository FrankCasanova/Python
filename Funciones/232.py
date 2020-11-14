# desing a functiont that reveives a list and
# returns a list whose content is the
# original list concatenated with an
# inverted versión of itself.
# the original list should not be modified


def reverse_concatenated(a_list):
    """
    returns a list whose content is
    the original list concatenated with an
    inverted versión of itself
    >>> reverse_concatenated([1,2,3])
    [3, 2, 1, 3, 2, 1]
    """

    doubling = a_list + a_list
    reverse = doubling[::-1]

    return reverse


my_list = [1, 2, 3, 4, 5]

print(my_list)
print(reverse_concatenated(my_list))
