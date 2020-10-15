# design a function that recives a string and
# returns true if it starts with lowercase and fase otherwise

def is_lower(x):

    lowerString = x.lower()

    if x[0] == lowerString[0]:
        return True
    return False


string = 'Hola yo me llamo manuela'

print(is_lower(string))
