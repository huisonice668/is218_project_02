from Randoms.NoSeedInt import noSeedInt
from random import seed


def withSeedIntList(low, high, count, seedValue):
    result = []
    seed(seedValue)
    for i in range(count):
        value = noSeedInt(low, high)
        result.append(value)

    return result
