# desins a function that tells us how much
# percent of the initial capital we will
# have to pay in interest when fully amortizing the
# mortgage. if it suits you
# you can use the functions you defined in the previous
# exercises.
# note: with the data from the previous example,
# we will pay a total interest of 40.01%
# because 60_015 is 40.01% of 150_000

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


def finalPay(quote):
    """
    calculate the final pay
    """
    return quote*12*(15)


def totalInterest(mortgag):
    """
    calculate how much interest we have paid
    """
    return finalPay(quote(mortgage, interest)) - mortgag


def totalPercentage(mortgage):
    """
    calculate the total percentage  you have paid
    """
    return (totalInterest(mortgage) * 100) / mortgage


# dates
mortgage = 150_000
interest = 4.75

print(quote(mortgage, interest))
print(finalPay(quote(mortgage, interest)))
print(totalInterest(mortgage))
print(totalPercentage(mortgage))
