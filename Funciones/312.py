# desing a function that receives two list and returns the
# elemets that belong to the first but not to the second
# without repeating eny sets difference.


def difference(list1, list2):

    difference = list(set(list1) - set(list2))

    return difference


list_a = [1, 2, 1]
list_b = [2, 3, 2, 4]

print(difference(list_a, list_b))
