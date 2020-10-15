# defines a function that converts degrees farenheit to dregrees celsius.

def converToCentigrades(x):
    return(x - 32) * (5 / 9)


temperature = 80

print(converToCentigrades(temperature))
