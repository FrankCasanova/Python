# Desing a function that tells you where the longest series in a list begins.
# in the exple form the previous exercise, the longest series begins at position
# 2 (which is the index where 8 appears)
# (note, if there are 2 series of equal length and this is the longest,
# you must return the position of the first of the series)

def positionMaxLenSerie(l):

    position = 0
    maximCounts = 0
    test = []

    for index, target in enumerate(l):

        if target not in test:
            test.append(target)

            if l.count(target) > maximCounts:
                maximCounts = l.count(target)
                position = index
    return position


a_list = [8, 2, 2, 9, 9]

print(positionMaxLenSerie(a_list))
