import unittest
import statistics

from Statistics.Statistics import Statistics
from Statistics.GenerateRandom import GenerateRandom

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()
        rand = GenerateRandom()

    def test_instantiate_statisctis(self):
        self.assertIsInstance(self.statistics, Statistics)

    #test mean by generate random low, high, seed value, and number of values
    # test case 1: with seed, integers list
    # test case 2: with seed, float list
    def test_mean(self):
        rand = GenerateRandom()
        for i in range(2):
            rand_low = rand.no_seed_integers(0,10)
            rand_high = rand.no_seed_integers(11, 20)
            rand_seed = rand.no_seed_integers(1, 5)
            rand_count = rand.no_seed_integers(0, 20)

            # test case 1: integer list
            if i == 0:
                randomIntList = rand.with_seed_integers_list(rand_low, rand_high, rand_count, rand_seed)

            # test case 2: float list; results of mean will be rounded to 8 digits
            if i == 1:
                randomIntList = rand.with_seed_floats_list(rand_low, rand_high, rand_count, rand_seed)

            myResult = round(self.statistics.mean(randomIntList), 8)
            realResult = round(statistics.mean(randomIntList), 8)
            self.assertEqual(myResult, realResult)


    def test_median(self):
        pass

    def test_sample_mean(self):
        pass


if __name__ ==  '__main__':
    unittest.main()
