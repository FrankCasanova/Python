# desing a function that receives a lists and returns
# the elements that belong to one or the other, but without
# repeating anything (unión of sets)
# example: if you receive lists [1,2,1] and [2,3,2,4]
# it will return list [1,2,3,4]


def union(list1, list2):
    # list_to_set = list1 + list2
    #list_to_set = set(list1 + list2)
    return list(set(list1) | set(list2))


list_a = [1, 2, 1]
list_b = [2, 3, 2, 4]

print(union(list_a, list_b))
