# we can also recursively formulate the sum of the first n natural numbers

def factorial(num):
    """
    docstring
    """
    if num == 0 or num == 1:
        result = 1
    elif num > 1:
        result = num + summation(num-1)
    return result


def summation(num):
    """
    docstring
    """
    return int(sum([value for value in range(1, num+1)]))


print(factorial(10))
