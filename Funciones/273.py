# desing a function that returns the absolute value of the maximum difference between
# 2 consecutive elements in a list. for example, the return value for list
# [1,10,2,6,2,0,] is 10, since it is the difference vetween the value 10 and 0.
# (tip: it may be convenient for you to know the maximun and minimum value of the list)


def max_difference(array):

    candidate = 0

    for i, t in enumerate(array):

        if i == len(array) - 1:
            break

        if t >= array[i+1]:
            difference = t - array[i+1]
            if difference > candidate:
                candidate = difference
        else:
            difference = array[i + 1] - t
            if difference > candidate:
                candidate = difference

    return candidate


a_list = [9, 34, 6, 3, 1, 65, 7, 3, 44, 5, 99, 7,
          3, 4, 55, 6, 6, 6, 777, 333, 45, 7, 345, 7, ]

print(max_difference(a_list))
