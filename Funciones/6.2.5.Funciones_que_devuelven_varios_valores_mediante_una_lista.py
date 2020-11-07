# example of the book.

def minmax(a, b, c):
    # calculate the minimum
    if a < b:
        if a < c:
            mini = a
        else:
            mini = b

    else:
        if b < c:
            mini = b
        else:
            mini = c

    # Calculating the maximum.
    if a > b:
        if a > c:
            maxi = a
        else:
            maxi = c
    else:
        if b > c:
            maxi = b
        else:
            maxi = c

    return [mini, maxi]


a = minmax(10, 2, 5)
print(f'el mínimo es {a[0]} ')
print(f'el máximo es {a[1]} ')
