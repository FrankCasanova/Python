# not all functions have a single parameter.
# we're now going to define one with two
# parameter: a function that returns the value
# of the area of a rectangle given its height
# and width


def rectangle_area(height, width):
    return height * width

# note that the different parameters of a
# function must be a separated by commas.
# when using the function, the arguments
# must also be separated by commas.


print(rectangle_area(3, 4))
