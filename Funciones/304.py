# we are going to buy a home and for that
# we will need a mortgage. the monthly
# installment m that we have to pay to secure a
# mortgage is h euros over n years at compound interes of i percent
# per year, it is calculated with the formula (look book)

# define a functiont that calculates the quota (founded to 2 decimal places)
# given h,n and i. uses as many local variables as you consider appropriate
# but at least r must appear in the expression whose value is returned and
# must first be calculated and stored in a
# local variable.
# note:
# yo can check the validity of a function knowing that you have to pay
# the amount of 1166.75e per month to pay off a 150000e mortgage in 15 years
# at an annual interest of 4.45%

# calculate r

def r(interest):
    return interest/(100*12)


def quote(mortgage, interest):
    """
    calculate the quote. the forumula appear on the book/
    """
    re = r(interest)
    quote = round(mortgage*re/(1-(1+re)**(-12*15)), 2)

    return quote


# dates
mortgage = 150_000
interest = 4.75

print(quote(mortgage, interest))
