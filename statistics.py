from typing import List


from math import sqrt


def mean(a_list):
    """
    docstring
    """
    adds = sum([element for element in a_list])
    return adds / len(a_list)


def variance(a_list):

    m = mean(a_list)
    adds = sum([(((element - m)**2) for element in a_list)])
    return adds / len(a_list)


def typical_defiation(a_list):
    """
    docstring
    """
    return sqrt(variance(a_list))
