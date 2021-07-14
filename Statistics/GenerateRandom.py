from random import random, randint, seed
from Randoms.NoSeedInt import noSeedInt
from Randoms.NoSeedFloats import noSeedFloats
from Randoms.WithSeedInt import withSeedInt

class GenerateRandom():
    num = 0;

    def __init__(self):
        pass

    # random number without a seed- integers
    def no_seed_integers(self, low, high):
        self.num = noSeedInt(low, high)
        return self.num

    # random number with a seed- floats
    def no_seed_floats(self, low, high):
        self.num = noSeedFloats(low, high)
        return self.num

    def with_seed_integers(self, low, high, seedValue):
        self.num = withSeedInt(low, high, seedValue)
        return self.num

    # random number with a seed- floats
    def with_seed_floats(self, low, high):
        pass
    # generate a list of N random numbers with a seed - integers
    def with_seed_integers_list(self, low, high, count):
        pass
    # generate a list of N random numbers with a seed - floats
    def with_seed_floats_list(self, low, high, count):
        pass