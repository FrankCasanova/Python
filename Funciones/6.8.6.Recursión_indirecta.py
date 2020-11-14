def par(n):
    """
    docstring
    """
    if n == 0:
        return True
    else:
        return impar(-1)


def impar(n):
    """
    docstring
    """
    if n == 0:
        return False
    else:
        return par(-1)


print(par(4))
