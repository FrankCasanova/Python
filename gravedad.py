from math import sqrt

g = 6.67e-11
mEarth = 5.97e24
rEarth = 6.37e6
mMoon = 7.35e22
rMoon = 1.74e6


def gravity_force(mass1, mass2, radius):
    """
    docstring
    """
    return g * mass1 * mass2 / radius**2


def distance(mass1, mass2, f):
    """
    docstring
    """
    return sqrt(g*mass1*mass2 / f)


def escape_velocity(mass1, r):
    """
    docstring
    """
    return sqrt(2*g*mass1 / r)


evEarth = escape_velocity(mEarth, rEarth)
evMoon = escape_velocity(mMoon, rMoon)
