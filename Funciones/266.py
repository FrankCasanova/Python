# defines a function that returns the number of days in a given year.
# note that a year is a leap year if it is divisible by 4 nad not divisible by 100,
# except if it is also divisible by 400, in which case it is leap

def is_leap(year):

    leap = False

    if year % 4 == 0:
        leap = True

    if year % 100 == 0 and year % 400:
        leap = True

    return leap


print(is_leap(2002))
