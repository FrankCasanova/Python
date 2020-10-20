# desing a function that returns the absolute value of the maximum diffenrece
# between two consecutive elements of a list.
# it may be convenient to know the maximum and minimum value of the list


def max_difference(array):

    value_a = max(array)
    value_b = min(array)

    return value_a - value_b


a_list = [56, 5, 4, 5, 56, 77, 6, 4, 5, 6, 3, 5, 654, 3, 4,
          43, 56, 87, 2134, 87, 567, 65, 3, 5, 4, 76, 3, 54, 8, 65,
          45, 56, 76, 34, 5, 86, 234, 6, 45, 123, 87, 456]


print(max_difference(a_list))
