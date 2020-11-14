def bits(num):
    """
    docstring
    """
    if num == 0 or num == 1:
        result = 1
    else:
        result = 1 + bits(num//2)

    return result


print(bits(63))
