import unittest
import statistics

from Statistics.Statistics import Statistics
from Statistics.GenerateRandom import GenerateRandom

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_statisctis(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        rand = GenerateRandom()
        randomIntList = rand.with_seed_integers_list(2, 10, 6, 2,)
        myResult = self.statistics.mean(randomIntList)
        realResult = statistics.mean(randomIntList)
        self.assertEqual(myResult, realResult)



    def test_median(self):
        pass
    def test_sample_mean(self):
        pass


if __name__ ==  '__main__':
    unittest.main()
