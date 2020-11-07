# give a function that, given a list of numbers,
# returns another list that only includes their odd numbers

def odd_numbers(list1):
    return [i for i in list1 if i % 2 != 0]


list_a = [3, 4, 5, 45, 2, 34, 2, 1, 53, 4, 643, 45, 23, 2, 4, ]

print(odd_numbers(list_a))
