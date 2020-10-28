# implements a python procedure susch that, given an integer,
# its figures in reverse order. for exaple, if the procedure
# receives the number 324, it will display 4, 2 and 3
# (on different lines)


def reverse(n):
    reverse = int(str(n)[::-1])
    return reverse


def display(n):

    show = str(reverse(n))

    for i in show:
        print(i)


display(5342)
