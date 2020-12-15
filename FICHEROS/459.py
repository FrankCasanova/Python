# design a program that takes the first 100 primer numbers
# and stores them in a text file called primo.txt

with open('primo.txt', 'w') as file:

    prime = [i for i in range(1, 101)
             if all(i % j != 0 for j in range(2, i))]

    file.write(str(prime))
