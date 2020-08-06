#programa que sustituya los elementos negativos por 0.

a = [1,-5,2,3,4,-3,2]

for i in range(len(a)):
    if a[i] < 0:
        a[i] = 0
print(a)         