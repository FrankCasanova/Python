# desing a function that reveives a list and
# returns another list whose content is the
# original list but with its components in
# reverse order. The original list should not
# be modified.


def reverse_list(a_list):
    """
    return another list whose content is the
    original list but with its components in
    reverse order
    >>> reverse_list([1, 2, 3])
    [3, 2, 1]
    """
    reverse = a_list[::-1]

    return reverse


my_list = [2, 3, 4]

print(my_list)
print(reverse_list(my_list))
