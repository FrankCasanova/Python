# bits = input('Dame un número binario: ')

# n = len(bits)

# valor = 0

# for bit in bits:
#     if bit == '1':
#         valor = valor + 2 ** (n - 1)

#     n -= 1

# print('Su valor decimal es: ', valor)

# bits = input('Dame los bits: ')

# valor = 0

# for bit in bits:
#     if bit == '1':
#         valor = 2 * valor + 1
#     else:
#         valor = 2 * valor

# print('Su valor decimal es: ', valor)

# bits = input('código binario: ')

# valor = 0

# for bit in bits:

#     if bit == '1':
#         valor += valor + 1
#     else:
#         valor += valor

# print('Su valor decimal es: ', valor)

bits = input('Dame un número binario: ')

valor = 0
for bit in bits:
    valor += valor + int(bit)
print('Su valor decimal es: ', valor)
