# defines a functions that convert degrees to radians.

from math import pi


def convertToRadians(x):
    return (x * pi) / 180


degrees = 200

print(convertToRadians(degrees))
