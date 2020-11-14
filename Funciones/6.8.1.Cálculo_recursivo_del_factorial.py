def factorial(number):
    """
    docstring
    """
    if number == 0 or number == 1:
        result = 1
    elif number > 1:
        result = number * factorial(number-1)

    return result


print(factorial(5))
