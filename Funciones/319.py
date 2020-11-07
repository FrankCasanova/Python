def modified(a, b):
    for element in b:
        a.append(element)
    b = b+[4]
    a[-1] = 100
    del b[0]
    return b[:]


list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = modified(list_a, list_b)

print(list_a)
print(list_b)
print(list_c)
