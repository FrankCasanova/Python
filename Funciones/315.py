# design a function that given a list of numbers, returns
# anorther list with only those nymbers from the first that are prime


def list_prime(list1):
    return [i for i in list1 if all(i % j != 0 for j in range(2, i))]


list_a = [4, 54, 34, 2, 3, 4, 6565, 34, 6, 4,
          43, 54, 23, 4, 56, 34, 53, 22, 1, 42, 6, ]

print(list_prime(list_a))
