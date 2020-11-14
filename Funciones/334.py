# desing a function that receives a list and returns
# a copy of the list with its elements
# ordered from lowest to highest, the original list
# should bot be modified


def sort_reverse(a_List):
    """
    sort it and reverse it a list
    """
    sort = sorted(a_List)

    return list(reversed(sort))


my_list = [3, 2, 7, 4, 54, 1, 2]

print(my_list)
print(sort_reverse(my_list))
