def mini(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


def maxi(n1, n2):
    if n2 < n1:
        return n1
    else:
        return n2


def mcd(m, n):
    mini = min(m, n)
    maxi = max(m, n)
    rest = maxi % mini

    if rest == 0:
        return mini
    else:
        return mcd(mini, rest)


print(mcd(500, 218))
