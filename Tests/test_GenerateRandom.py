import unittest

from Statistics.GenerateRandom import GenerateRandom


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.generateRandom = GenerateRandom()

    def test_instantiate_generateRandom(self):
        self.assertIsInstance(self.generateRandom, GenerateRandom)

    def test_no_seed_integers(self):
        print(self.generateRandom.no_seed_integers(0, 10))



if __name__ ==  '__main__':
    unittest.main()
