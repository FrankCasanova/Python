# examplo from the book.

from math import sqrt, asin, pi
import doctest


def triangle_area(a, b, c):
    '''
    return the area of a triangle, given 3 dates
    >>> triangle_area(10,20,20)
    96.82
    '''

    s = (a+b+c)/2
    return round(sqrt(s*(s-a)*(s-b)*(s-c)), 2)


def alfa_angle(a, b, c):
    '''
    return the value of the angle alfa
    >>> alfa_angle(10,20,20)
    28.95
    '''
    s = triangle_area(a, b, c)
    return round(180/pi*asin(2*s/(b*c)), 2)


def menu():
    """
    user menu
    """
    option = 0
    while option != 1 and option != 2:
        print('1) Calculate the area of a triangle.')
        print('2) calculate the angle opposite the first side. ')
        option = int(input('choose an option.'))
    return option


side1 = 5
side2 = 4
side3 = 3

s = menu()

if s == 1:
    outcome = triangle_area(side1, side2, side3)
else:
    outcome = alfa_angle(side1, side2, side3)

print('your choose was the option', s)
print('the outcome is', outcome)


# doctest.testmod()
