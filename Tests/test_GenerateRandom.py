import unittest

from Statistics.GenerateRandom import GenerateRandom


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.generateRandom = GenerateRandom()

    def test_instantiate_generateRandom(self):
        self.assertIsInstance(self.generateRandom, GenerateRandom)

    def test_no_seed_integers(self):
        #print(self.generateRandom.no_seed_integers(0, 10))
        pass

    def test_no_seed_floats(self):
        #print(self.generateRandom.no_seed_floats(0.0, 10.0))
        pass

    def test_with_seed_integers(self):
        for i in range(5):
            self.assertEqual(self.generateRandom.with_seed_integers(0, 10, 6), self.generateRandom.with_seed_integers(0, 10, 6))
            self.assertEqual(self.generateRandom.with_seed_integers(20, 99, 8), self.generateRandom.with_seed_integers(20, 99, 8))

    def test_with_seed_floats(self):
        for i in range(5):
            self.assertEqual(self.generateRandom.with_seed_floats(0.0, 10.0, 6), self.generateRandom.with_seed_floats(0.0, 10.0, 6))
            self.assertEqual(self.generateRandom.with_seed_floats(20.0, 99.0, 8), self.generateRandom.with_seed_floats(20.0, 99.0, 8))

    def test_with_seed_integers_list(self):
        for i in range(3):
            #print(self.generateRandom.with_seed_integers_list(2, 20, 6, 8))
            #print(self.generateRandom.with_seed_integers_list(3, 25, 6, 8))
            self.assertEqual(self.generateRandom.with_seed_integers_list(2, 20, 6, 8), self.generateRandom.with_seed_integers_list(2, 20, 6, 8))
            self.assertEqual(self.generateRandom.with_seed_integers_list(3, 25, 6, 8), self.generateRandom.with_seed_integers_list(3, 25, 6, 8))

    def test_with_seed_floats_list(self):
        for i in range(3):
            #print(self.generateRandom.with_seed_floats_list(2.0, 20.0, 6, 8))
            #print(self.generateRandom.with_seed_floats_list(3.0, 25.0, 6, 8))
            self.assertEqual(self.generateRandom.with_seed_integers_list(2, 20, 6, 8), self.generateRandom.with_seed_integers_list(2, 20, 6, 8))
            self.assertEqual(self.generateRandom.with_seed_integers_list(3, 25, 6, 8), self.generateRandom.with_seed_integers_list(3, 25, 6, 8))

if __name__ ==  '__main__':
    unittest.main()
