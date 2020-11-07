# design a function that takes the three
# coefficients of a quadratic equation equation of
# the form ax2 + bx + c = 0 and returns a list
# of their real solutions. if the equiation only has
#  on real solution, it returns a list with
# 2 copies of it. if it has no real solution or
# if it has infinite solutions, it returns a list
# with 2 copies of the none value.

from math import sqrt


def quadratic_equation(a, b, c):
    # we make calculations if there is a solution
    if a != 0:
        if b**2 - 4*a*c >= 0:
            x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
            x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
            if x1 == x2:
                return [x1, x1]
            else:
                return [x1, x2]
    else:
        return [None, None]


num1, num2, num3 = 1, 2, 0

print(quadratic_equation(num1, num2, num3))
