# what happens to the central element of the
# list when the list has an odd number of elements?
# does our function invert correctly?


def invert(list1):
    """
    docstring
    """

    # for i in range(len(list1)//2):
    #     c = list1[i]
    #     list1[i] = list1[len(list1)-1-i]
    #     list1[len(list1)-1-i] = c

    list1 = list1.reverse()


a = [1, 2, 3, 4, 5, 6, 7]

invert(a)

print(a)


# yes hahaha
