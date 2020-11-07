# desing a function that receives 2 lists and returns the
# elements common to both, without repeating any (intersection of set)
# example: if it reveives list [1,2,1] and [2,3,2,4] it will return
# list [2]


def intersection(list1, list2):

    # for i in list1:
    #     for j in list2:
    #         if i == j and i not in common:
    #             common.append(i)

    return list(set(list1) & set(list2))


list_a = [1, 2, 1]
list_b = [2, 3, 2, 4]

print(intersection(list_a, list_b))
