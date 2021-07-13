import unittest

#from Calculator.Calculator import Calculator
from Calculator.Statistics import Statisctis


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statisctis = Statisctis()

    def test_instantiate_statisctis(self):
        self.assertIsInstance(self.statisctis, Statisctis)

    def test_mean(self):
        pass

    def test_median(self):
        pass
    def test_sample_mean(self):
        pass


if __name__ ==  '__main__':
    unittest.main()
