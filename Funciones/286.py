# desing a function that tells(by returning true or false)
# whether two numers are fiends. two numbers are friends
# if the sum of the divisor of the first (excluding him)
# is egual to the second and viceversa.

import numpy as np


def are_friends(num1, num2):

    sum_div_num1 = 0
    sum_div_num2 = 0

    for i, o in zip(range(1, num1), range(1, num2)):

        if num1 % i == 0:
            sum_div_num1 += i

        if num2 % o == 0:
            sum_div_num2 += o

    return sum_div_num1 == num2 and sum_div_num2 == num1


a = 2620

b = 2924

print(are_friends(a, b))
