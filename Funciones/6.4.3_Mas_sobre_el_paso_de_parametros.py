# book example

# def increase(p):
#     p = p+1
#     return p


# a = 1
# b = increase(a)

# print('a: ', a)
# print('b: ', b)

def modified(a, b):
    a.append(4)  # points to a varible
    b = b+[4]   # create a new variable and point to it
    return b


list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = modified(list_a, list_b)

print(list_a)
print(list_b)
print(list_c)
