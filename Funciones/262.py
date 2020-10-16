# design a function called is_repetition that receives a string
# and tells us if the string is formed by cocatenating a string with itself

def is_repetition(x):

    outcase = False

    for i in range(len(x)):

        if outcase:
            break

        if i == 0:  # ignoring the first step
            continue
        if len(x) % i != 0:   # test if the string is pair
            continue

        if len(x) % i == 0:

            for j in range(0, i + 1):  # this indicates which number should be multiplied by

                # and this test that the string isn't longer than original string
                if len(x[:i]*j) <= len(x):

                    if x[:i] * j == x:
                        outcase = True
                        break
                else:
                    break

    return outcase


string = 'asdffdsaasdffdsaasdffdsa'

print(is_repetition(string))
