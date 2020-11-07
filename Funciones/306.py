# desing a function that tells us how much
# interest (in euros) we will have finally paid to the
# bank if we open a mortgage
# of h euros at an interest of i per hundred in n years.
# if it suits you, you can use the functions you defined in the previous
# exercise
# note:
# with the data from the previous example, we sill have paid a total of
# 210_015 - 150_000 = 60_015


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


# dates
mortgage = 150_000
interest = 4.75

print(quote(mortgage, interest))
print(finalPay(quote(mortgage, interest)))
print(totalInterest(mortgage))
