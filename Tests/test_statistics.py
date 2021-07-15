import unittest
import statistics

from Statistics.Statistics import Statistics
from Statistics.GenerateRandom import GenerateRandom


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_statisctis(self):
        self.assertIsInstance(self.statistics, Statistics)

    # test mean by generate random low, high, seed value, and number of values
    # test case 1: with seed, integers list
    # test case 2: with seed, float list
    def test_mean(self):
        rand = GenerateRandom()
        for i in range(2):
            rand_low = rand.no_seed_integers(0, 10)
            rand_high = rand.no_seed_integers(11, 20)
            rand_seed = rand.no_seed_integers(1, 5)
            rand_count = rand.no_seed_integers(0, 20)

            # test case 1: integer list
            if i == 0:
                randomList = rand.with_seed_integers_list(rand_low, rand_high, rand_count, rand_seed)

            # test case 2: float list; results of mean will be rounded to 8 digits
            if i == 1:
                randomList = rand.with_seed_floats_list(rand_low, rand_high, rand_count, rand_seed)

            # test if the program will throw an exception if the list is empty
            if len(randomList) == 0:
                self.assertRaises(ValueError)
            else:
                # print(randomList)
                myResult = round(self.statistics.mean(randomList), 8)
                realResult = round(statistics.mean(randomList), 8)
                self.assertEqual(myResult, realResult)

    def test_median(self):
        rand = GenerateRandom()
        for i in range(2):
            rand_low = rand.no_seed_integers(2, 7)
            rand_high = rand.no_seed_integers(11, 23)
            rand_count = rand.no_seed_integers(0, 10)
            rand_seed = rand.no_seed_integers(3, 5)

            # test case 1: integer list
            if i == 0:
                randomList = rand.with_seed_integers_list(rand_low, rand_high, rand_count, rand_seed)

            # test case 2: float list; results of mean will be rounded to 8 digits
            if i == 1:
                randomList = rand.with_seed_floats_list(rand_low, rand_high, rand_count, rand_seed)

            # test if the program will throw an exception if the list is empty
            if len(randomList) == 0:
                self.assertRaises(ValueError)
            else:
                # print(randomList)
                myResult = round(self.statistics.median(randomList), 8)
                realResult = round(statistics.median(randomList), 8)
                self.assertEqual(myResult, realResult)

    def test_mode(self):
        rand = GenerateRandom()

        rand_low = rand.no_seed_integers(1, 3)
        rand_high = rand.no_seed_integers(4, 50)
        rand_count = rand.no_seed_integers(0, 30)
        rand_seed = rand.no_seed_integers(3, 8)

        randomList = rand.with_seed_integers_list(rand_low, rand_high, rand_count, rand_seed)

        if len(randomList) == 0:
            self.assertRaises(ValueError)
        else:
            myResult = self.statistics.mode(randomList)
            realResult = statistics.mode(randomList)
            self.assertEqual(myResult, realResult)

    def test_sample_var(self):
        rand = GenerateRandom()

        for i in range(2):
            rand_low = rand.no_seed_integers(0, 5)
            rand_high = rand.no_seed_integers(6, 20)
            rand_seed = rand.no_seed_integers(2, 9)
            rand_count = rand.no_seed_integers(2, 20)

            # test case 1: integer list
            if i == 0:
                randomList = rand.with_seed_integers_list(rand_low, rand_high, rand_count, rand_seed)

            # test case 2: float list; results of mean will be rounded to 8 digits
            if i == 1:
                randomList = rand.with_seed_floats_list(rand_low, rand_high, rand_count, rand_seed)

            # test if the program will throw an exception if the list is empty
            if len(randomList) == 0:
                self.assertRaises(ValueError)
            else:
                myResult = self.statistics.sample_var(randomList)
                realResult = statistics.variance(randomList)
                self.assertEqual(round(myResult, 8), round(realResult, 8))

    def test_sample_sd(self):
        rand = GenerateRandom()

        for i in range(2):
            rand_low = rand.no_seed_integers(0, 5)
            rand_high = rand.no_seed_integers(6, 20)
            rand_seed = rand.no_seed_integers(2, 9)
            rand_count = rand.no_seed_integers(5, 20)

            # test case 1: integer list
            if i == 0:
                randomList = rand.with_seed_integers_list(rand_low, rand_high, rand_count, rand_seed)

            # test case 2: float list; results of mean will be rounded to 8 digits
            if i == 1:
                randomList = rand.with_seed_floats_list(rand_low, rand_high, rand_count, rand_seed)

            # test if the program will throw an exception if the list is empty
            if len(randomList) == 0:
                self.assertRaises(ValueError)
            else:
                # print(randomList)
                myResult = round(self.statistics.sample_sd(randomList), 8)
                realResult = round(statistics.stdev(randomList), 8)
                # print('my result = ', myResult)
                # print('real result = ', realResult)
                self.assertEqual(myResult, realResult)

    def test_confidence_interval(self):
        pass

    def test_margin_of_error(self):
        pass
    '''''''''''
    def test_confidence_interval(self):
        rand = GenerateRandom()

        for i in range(2):
            rand_low = rand.no_seed_integers(0, 2)
            rand_high = rand.no_seed_integers(3, 100)
            rand_seed = rand.no_seed_integers(2, 9)
            rand_count = rand.no_seed_integers(5, 20)
            #rand_z = rand.no_seed_floats(1.2, 3.3)

            # test case 1: integer list
            if i == 0:
                randomList = rand.with_seed_integers_list(rand_low, rand_high, rand_count, rand_seed)

            # test case 2: float list; results of mean will be rounded to 8 digits
            if i == 1:
                randomList = rand.with_seed_floats_list(rand_low, rand_high, rand_count, rand_seed)

            # test if the program will throw an exception if the list is empty
            if len(randomList) == 0:
                self.assertRaises(ValueError)
            else:
                #print(randomList)
                myResult = round(self.statistics.confidence_interval(randomList, 1.645), 8)
                realResult = st.t.interval(alpha=0.95, df=len(randomList)-1, loc=np.mean(randomList), scale=st.sem(randomList))
                print('my result = ', myResult)
                print('real result = ', realResult)
                self.assertEqual(myResult, realResult)

    def test_sample_mean(self):
        rand = GenerateRandom()
        sample_size = rand.no_seed_integers(0, 20)
        mean_of_each_sample = []
        for i in range(2):
            rand_low = rand.no_seed_integers(1,3)
            rand_high = rand.no_seed_integers(4, 15)
            rand_count = rand.no_seed_integers(0, 10)
            rand_seed = rand.no_seed_integers(3, 5)
            # test case 1: integer list
            if i == 0:
                randomList = rand.with_seed_integers_list(rand_low, rand_high, rand_count, rand_seed)
            # test case 2: float list; results of mean will be rounded to 8 digits
            if i == 1:
                randomList = rand.with_seed_floats_list(rand_low, rand_high, rand_count, rand_seed)
        # check empty list
        with self.assertRaises(ValueError):
            self.statistics.sample_mean(randomList, 0)
        # check sample size greater than population size
        with self.assertRaises(Exception):
            self.statistics.sample_mean(randomList, 20)
        realResult = statistics.mean(self.statistics.getSample(randomList))
        self.statistics.sample_mean(randomList, sample_size) 
        print(myResult)
    '''''''''


if __name__ == '__main__':
    unittest.main()
