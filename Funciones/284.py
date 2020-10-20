# define a function called nth root that returns
# the value of the root of x (note:
# remember that the nth root is x raised to 1/n)


def nth_root(x, n):
    return x ** (1 / n)


root = 34
nth = 3

print(nth_root(root, nth))
