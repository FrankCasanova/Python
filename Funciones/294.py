# dising an is_prime function that determines whether a number is prime
# returning true or not returning false. next desing a sample_primes procedure
# that receives a number and displays all prime numbers between 1 and that number
# on the screen

def is_prime(n):

    prime = True  # firs, we assume it is prime
    for i in range(2, n):
        if n % i == 0:
            prime = False

    return prime


def sample_primes(n):

    for i in range(1, n):
        if is_prime(i):
            print(f'the number {i} is prime')


sample_primes(10)
