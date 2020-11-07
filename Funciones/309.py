# desins a procedure that shows on the
# screen the total capital paid to the bank for a mortage
# of h euros at i% annual interest for 10, 15, 20 and 25 years.
# (if it suits your, substract how the functions you designed as
# a solution to the previous exercices)

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


def variousYears(interest, mortgage):
    """
    calculate the total quote to pay for a mortgage
    for a capital of H euros at i% annual interest 
    for 10, 15, 20 and 25 years.
    """
    listYears = [10, 15, 20, 25]

    for year in listYears:
        print(f'para {year} años la cuota es de : ', round(
            mortgage*r(interest)/(1-(1+r(interest))**(-12*year)), 2))


def differentFinalPays(mortgage, interest):
    """
    shows the total capital paid in differents
    range of years
    """
    listYears = [10, 15, 20, 25]

    for year in listYears:
        print(f'para {year} años habrás pagado: ',
              quote(mortgage, interest)*12*year)


# dates
mortgage = 150_000
interest = 4.75

print(quote(mortgage, interest))
print(finalPay(quote(mortgage, interest)))
print(totalInterest(mortgage))
print(totalPercentage(mortgage))
variousYears(interest, mortgage)
differentFinalPays(mortgage, interest)
