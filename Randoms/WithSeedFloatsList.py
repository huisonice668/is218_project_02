from random import seed
from Randoms.NoSeedFloats import noSeedFloats

def withSeedFloatsList(low, high, count, seedValue):
    result = []
    seed(seedValue)
    for i in range(count):
        value = noSeedFloats(low, high)
        result.append(value)
    return result