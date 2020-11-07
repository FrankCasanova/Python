# desings a function that, given a list of numbers, returns a
# list with all the pairs of numbers that we can form with one from
# the first list and another form the second.
# for example, if lists [1,2,5] and [2,5] are supplied the
# resulting list is [[1,2], [1,5],[3,2],[3,5],[5,2],[5,5]]


def pairs(list1, list2):
    """
    return the possibles combination from both list
    """
    combinations = [[i, j] for i in list1 for j in list2]
    # for i in list1:
    #     for j in list2:
    #         combinations.extend([[i,j]])

    return combinations


list_a = [1, 3, 5]
list_b = [2, 5]


print(pairs(list_a, list_b))
