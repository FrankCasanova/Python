# desing a function that computes the proucer
# given a and b. if a is greater than b
# the funtion will return the value 0.
# if 0 is between a and b, the function will also return
# the value 0, but without the need to
# iterate through the loop


def producer(a, b):

    prod = 1

    if a > b:
        return 0
    elif a < 0:
        return 0
    else:
        for i in range(a, b + 1):
            prod *= i

    return prod


a = 4
b = 8

print(producer(a, b))
