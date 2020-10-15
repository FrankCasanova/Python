# defines a function that converts radians to degrees

from math import pi


def converToDegrees(x):
    return (x*180)/pi


radians = 1.4

print(converToDegrees(radians))
