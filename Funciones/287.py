# this exercise appears on the book.


def menu():

    option = ''

    while option not in 'abc' or len(option) != 1:

        print('atm')
        print('deposit money')
        print('withdraw money')
        print('check balance')

        option = input('choose a option')

        if len(option) != 1 or option not in 'abc':

            print('You can only choose a, b or c. Try again')

    return option


menu()
