# desing a function that calculates the sum of the difference between contiguous numbers
# in a list

def sumContiguous(L):

    plus = [(target - lista[index-1])
            for index, target in enumerate(lista) if index != 0]
    # for index, target in enumerate(lista):
    #     if index == 0:
    #         continue
    #     else:
    #         plus.append(target - lista[index - 1])

    plus = sum(plus)

    return plus


lista = [1, 3, 6, 10]

print(sumContiguous(lista))
