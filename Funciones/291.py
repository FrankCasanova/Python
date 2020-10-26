# when designing a board game, it would be good to have and «electronic dice»
# write a python function with no arguments called dice, which returns a random integer
# between 1 and 6.


import random


def dice():
    return random.randint(1, 6)


print(dice())
