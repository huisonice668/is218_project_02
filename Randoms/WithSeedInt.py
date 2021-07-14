from random import randint, seed

def withSeedInt(low, high, seedValue):
    seed(seedValue)
    result = randint(low, high)
    return result