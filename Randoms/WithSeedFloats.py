from random import seed
import random

def withSeedFloats(low, high, seedValue):
    seed(seedValue)
    result = random.uniform(low, high)
    return result