# desings a procedure that, given a list of numbers,
# modifies it so that only those numbers that are perfect
# survive the call

def perfect_numbers(list1):
    # aux = [i for i in list1 if int(
    #     sum([n for n in range(1, i) if i % n == 0])) == i]

    for number in list1:
        aux = 0
        for i in range(1, number):
            if number % i == 0:
                aux += i
        if aux != number:
            del list1[list1.index(number)]
            aux = 0
        else:
            aux = 0


mylist = [26, 6, 28, 13, 3, 6, 4, ]

perfect_numbers(mylist)

print(mylist)
