# defines a function called circle_area that, fro the radius of a circle,
# retur de value of its area. use the value 3.1416 as an approximation of pi
# or import the pi value that you will find in the pi module

from math import pi


def circleArea(x):
    return pi * (x ** 2)


radio = 6

print(circleArea(radio))
