# desing a no-argument function that returns a random nuber
# greater than or egual to 0.0 and less than 10.0
# you can call the function from random from your function


from random import *


def random_generator():
    return randint(0.0, 10.0)


print(random_generator())
