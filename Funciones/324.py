# an apprentice suggests this other solution.
# works?

def invert(list1):
    for i in range(len(list1)//2):
        c = list1[i]
        list1[i] = list1[-i-1]
        list1[-i-1] = c


a = [1, 2, 3, 4, 5, 6, 7]

invert(a)

print(a)


# yes
