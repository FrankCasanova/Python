
def invert(list1):
    for i in range(len(list1)//2):
        c = list1[i]
        list1[i] = list1[len(list1)-1-i]
        list1[len(list1)-1-i] = c


a = [1, 2, 3, 4]

invert(a)

print(a)
