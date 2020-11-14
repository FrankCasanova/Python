def fibonacci(n):
    """
    docstring
    """

    if n == 1 or n == 2:
        result = 1
    elif n > 2:
        result = fibonacci(n-1) + fibonacci(n-2)

    return result


print(fibonacci(10))
