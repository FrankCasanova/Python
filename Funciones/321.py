def modify_parameters(x, y):
    x = 1
    y.append(3)
    y = y+[4]
    y[0] = 10


a = 0
b = [0, 1, 2]
modify_parameters(a, b)
print(a)
print(b)
