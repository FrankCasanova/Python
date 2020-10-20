# desing a funtion that returns the solution
# of the linear equation ax + b = 0 given
# a and b. If the equation has infinites or
# has no solution, the funtion will detect it
# and return the value None


def first_degree_equation(a, b):

    if a != 0:
        x = -b / a
        return x

    elif a == 0:
        if b != 0:
            return None
        else:
            return None

    else:
        return None


a = 3
b = 5

print(first_degree_equation(a, b))
