import unittest


from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add(self):
        test_data = CsvReader('Tests/Data/addition.csv').data
       # pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(int(self.calculator.result), int(row['Result']))
        print('----------------------------end of addition tests--------------------------')

    def test_minus(self):
        print('----------------------in minus test ---------------')
        test_data2 = CsvReader('Tests/Data/subtraction.csv').data
        #pprint(test_data2)
        for row in test_data2:
            # result = Calculator.add(10, 5)
            # self.assertEqual(result ,15)

            self.assertEqual(self.calculator.minus(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(int(self.calculator.result), int(row['Result']))

    '''''''''
    def test_multiply(self):
       # test_data = CsvReader('src/multiplicationTests.csv').data
        #pprint(test_data)
        #for row in test_data:
         #   self.assertEqual(self, Calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
          #  self.assertEqual(self, Calculator.result, int(row['Result']))
        result = Calculator.multiply(5, 3)
        self.assertEqual(result, 15)

    def test_divide(self):
        result = Calculator.divide(3, 2)
        self.assertEqual(result, 1.5)
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)
        test_data = CsvReader('src/divisionTests.csv').data
        #for row in test_data:
            #self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), int(row['Result']))
           # self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square(self):
        result = Calculator.square(6)
        self.assertEqual(result, 36)
        #test_data = CsvReader('src/squaringTests.csv').data
        # for row in test_data:
        # self.assertEqual(self.calculator.square(row['Value 1'], row['Value 2']), int(row['Result']))
        # self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_root(self):
        result = Calculator.squareRoot(81)
        self.assertEqual(result, 9)
        #test_data = CsvReader('src/squareRootTests.csv').data
        # for row in test_data:
        # self.assertEqual(self.calculator.squareRoot(row['Value 1'], row['Value 2']), int(row['Result']))
        # self.assertEqual(self.calculator.result, int(row['Result']))

'''''''''''


if __name__ ==  '__main__':
    unittest.main()
