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


def are_friends(n):  # tell if two numbers are friends

    sum_div1 = 0
    sum_div2 = 0
    pairs = []

    for i in range(1, n):

        for j in range(1, i):
            if i % j == 0:
                sum_div1 += j

        if sum_div1 != i:
            for k in range(1, sum_div1):
                if sum_div1 % k == 0:
                    sum_div2 += k

        if i == sum_div2:
            if sum_div1 not in pairs:
                pairs.append(sum_div2)
                pairs.append(sum_div1)
                sum_div1 = 0
                sum_div2 = 0
        else:
            sum_div1 = 0
            sum_div2 = 0
    pairs = np.array(pairs)
    pairs = np.reshape(pairs, ((len(pairs)//2), 2))

    return print(pairs)


# def friendsNumers_list(): #show the list of friends numbers
numer = 10000  # limit number.


are_friends(numer)
