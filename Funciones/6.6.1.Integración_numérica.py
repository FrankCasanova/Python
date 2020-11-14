# # book example
# def integra_x2(a, b, n):
#     """
#     calculate the integral of a graphic
#     """
#     if n == 0:
#         summation = 0
#     else:

#         deltax = (a-b)/n
#         summation = int(sum([(deltax*(a+i*deltax)**2) for i in range(n)]))

#     return summation


# print(integra_x2(34, 65, 100))

# a = 2
# value = 1

# print(f'elevado {a}, {0} = {value}')

# for n in range(1, 8):
#     value = a*value
#     print(f'elevado {a}, {n} = {value}')

def exponencial(a, n):
    """
    docstring
    """
    numerador = 1
    denominador = 1
    sumatorio = 1.0
    for k in range(1, n):
        numerador = a*numerador
        denominador = k*denominador
        sumatorio += numerador/denominador
    return sumatorio


print(exponencial(2, 20))
