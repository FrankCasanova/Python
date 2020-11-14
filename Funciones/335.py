# desing a function that receives a matrix and,
# if it square (that is, it has the same number of rows as it has columns)
# return the sum of all its components arranged on the main diagonal
# (that is, all elements of the form Ai,i) if the matrix is not square,
# the functión will return none

import numpy as np


def sum_diagonal(a_matrix):
    """
    return the sum on the diagonal main
    """
    a = np.array(a_matrix)
    # print(a)
    # print(len(a))
    # print(len(a[:,1]))
    # print(len(a[1,:]))
    if len(a[:, 1]) == len(a[1, :]):
        return np.trace(a)
    else:
        return None


my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_diagonal(my_matrix))
