# desing a programa that, given a number n, displays all pairs
# of firndly numers less than n on thje screen. printing of
# results must be done from a procedure.
# two friendly numbers should only appear once per screen.
# for example, 220 and 284 are friends: if the message
# 220 and 284 are friends, the message 284 and 220 are
# friends will not appear, as it is redundant.
# you must desing a function that says if 2 numbers
# are friends and a procedure that displays the table

import numpy as np


def are_friends(num1, num2):  # tell if two numbers are friends

    sum_div_num1 = 0
    sum_div_num2 = 0

    for i, o in zip(range(1, num1), range(1, num2)):

        if num1 % i == 0:
            sum_div_num1 += i

        if num2 % o == 0:
            sum_div_num2 += o

    return sum_div_num1 == num2 and sum_div_num2 == num1


def display_pairs(n):

    n1 = 0
    n2 = 0

    pair_list = []
    for i in range(1, n + 1):
        n1 = i
        for j in range(1, i):
            if i % j == 0:
                n2 += j
        if n1 != n2 and n1 not in pair_list and are_friends(n1, n2):
            pair_list.append(n1)
            pair_list.append(n2)
        else:
            n2 = 0

    pair_list = np.array(pair_list)
    pair_list = np.reshape(pair_list, (len(pair_list)//2, 2))

    return print(pair_list)


# def friendsNumers_list(): #show the list of friends numbers
numer = 5000  # limit number.


display_pairs(numer)
