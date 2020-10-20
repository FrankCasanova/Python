# design a function that calculates summation b i=a
# given a and b if a is greater than b
# the function will return the value 0


def summation(a, b):

    plusses = 0

    if b < a:
        return plusses

    for i in range(1, b + 1):
        plusses += i

    return plusses


a = 2
b = 5000

print(summation(a, b))
