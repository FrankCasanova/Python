# what this program shows on the screen when it is executed

def try_to_interchange(a, b):
    """
    docstring
    """
    aux = a
    a = b
    b = aux


list1 = [1, 2]
list2 = [3, 4]

try_to_interchange(list1, list2)

print(list1)
print(list2)
