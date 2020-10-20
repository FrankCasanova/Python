def maximus(L):

    # to find the maximum we first sort the list and then take
    # the last value in the list, which sould be the largest

    if len(L) > 0:
        candidate = L.sort()
        candidate = L[len(aList)-1]
    else:
        candidate = None
    return candidate


aList = []

print(maximus(aList))
