# the triangle_area function that we have defined
# can cause an error at run time.
# if the argument of the calculated square root is its last
# line is a negative number, a domain error will be produced.
# have the function only call sqrt if its argument is greater than
# or equal to zero. it also detects possible problems in the alpha
# angle and modifies the function to avoid possible errors when executing
# the program

from math import sqrt, asin, pi


def triangle_area(a, b, c):
    s = (a+b+c) / 2
    try:
        return sqrt(s * (s-a) * (s-b) * (s-c))

    except ValueError:
        return 0


def alfa_angle(a, b, c):
    s = triangle_area(a, b, c)
    try:
        return 180/pi * asin(2 * s / (b*c))
    except ZeroDivisionError:
        return 0


def menu():
    option = 0
    while option != 1 and option != 2:
        print('1) Calculate the triangle area.')
        print('2) Calculate angle opposite to first side.')
        option = int(input('Choose an option: '))

    return option


side1 = 5.0  # float(input('Give me the side a: '))
side2 = 4.0  # float(input('Give me the side b: '))
side3 = 0.0  # float(input('Give me the side c: '))

s = menu()

if s == 1:
    result = triangle_area(side1, side2, side3)
else:
    result = alfa_angle(side1, side2, side3)

print(f'You chose the optión: {s}')
print(f'The result is: {result}')
