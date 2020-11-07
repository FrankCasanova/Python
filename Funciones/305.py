# desin a function that returns us the
# amount of euros that we will have finally
# paid to the bank if we open a mortgage of h
# euros at an interest of i per hundred in n years
# if it suits you, you can use the function
# you defined in the previous exercise.
# note with the data of the previous example
# we will have paid a total of 210_015euros.


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


# dates
mortgage = 150_000
interest = 4.75

print(quote(mortgage, interest))
print(finalPay(quote(mortgage, interest)))
