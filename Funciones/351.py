# modify the exponential2 function of the previous program
# so that the infeficientent calls to elevated and
# factorial are not effected.


def exponential(a, epsilon, n):
    """
    docstring
    """
    numerator = 1
    denominator = 1
    term = 1.0
    count = 0
    summation = 0.0
    for k in range(1, n):
        numerator = a*numerator
        denominator = k*denominator
        term += numerator / denominator
    while term > epsilon:
        summation += term
        count += 1
    return summation


print(exponential(5, 5.7, 7))
