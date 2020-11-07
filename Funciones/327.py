# desings a procedure that, given a list of numbers,
# modifies it so that only those numbers that are perfect
# survive the call

def perfect_numbers(list1):
    aux = [i for i in list1 if int(
        sum([n for n in range(1, i) if i % n == 0])) == i]


mylist = [26, 6, 28, 13, 3, 6, 4, ]

print(mylist)
