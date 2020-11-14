def f(x):
    """
    docstring
    """
    return x**2 - 2*x - 2


def bisection(a, b, epsilon):
    """
    docstring
    """

    # firs we test that f is not equal to 0
    if f(a) == 0:
        return None
    elif f(b) == 0:
        return None

    # second we test than both f have not positive value
    if f(a) > 0 and f(b) > 0:
        return None

    c = (a+b)/2  # at the center of the interval
    while f(c) != 0 and b-1 > epsilon:
        if f(a) * f(c) > 0:
            a = c
        elif f(b) * f(c) > 0:
            b = c
        c = (a+b)/2

    return c


print(f'El cero está en: ', bisection(0.5, 3.5, 1e-5))
