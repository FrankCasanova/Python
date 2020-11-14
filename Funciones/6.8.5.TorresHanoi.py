# exercise 369 has been included

def hanoi(n, inicial, final, libre):
    """
    docstring
    """
    global contador

    if n == 1:
        contador += 1
        print(f'Mover disco superior de aguja {inicial} a {final}.')

    else:
        # determinar cual aguja está libre
        # if inicial != 1 and final != 1:
        #     libre = 1
        # elif inicial != 2 and final != 2:
        #     libre = 2
        # else:
        #     libre = 3
        # # primer sub-problema: morver n-1 discos de inicial a libre.
        # hanoi(n-1, inicial, libre)
        # # transferir el fisco grande a su posición final.
        # print(f'Mover disco superior de aguja {inicial} a {final}')
        # # segundo sub-problema: mover n-1 discos de libre a final.
        # hanoi(n-1, final, inicial)

        hanoi(n-1, inicial, libre, final)

        print(f'Mover disco superior de aguja {inicial} a {final}')
        contador += 1

        hanoi(n-1, libre, final, inicial)


contador = 0

print(hanoi(5, 1, 3, 2))
print(contador)
