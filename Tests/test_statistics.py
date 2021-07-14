import unittest

#from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/UnitTestAddition.csv')

    def test_instantiate_statisctis(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        pass

    def test_median(self):
        pass
    def test_sample_mean(self):
        pass


if __name__ ==  '__main__':
    unittest.main()
