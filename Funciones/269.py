# desing a function that, fiven a list of integers, returns the number
# in it.

def series(lista):

    counts = []
    test = []

    for i in lista:

        if i not in test:
            test.append(i)
            counts.append(lista.count(i))

    return len(counts)


aList = [1, 1, 8, 8, 8, 8, 0, 0, 0, 2, 10, 10]

print(series(aList))
