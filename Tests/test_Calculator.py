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
        test_data = CsvReader('Tests/Data/UnitTestAddition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(int(self.calculator.result), int(row['Result']))

    def test_minus(self):
        test_data = CsvReader('Tests/Data/UnitTestSubtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.minus(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(int(self.calculator.result), int(row['Result']))

    def test_divide(self):
        test_data = CsvReader('Tests/Data/UnitTestDivision.csv').data
        for row in test_data:
            self.assertEqual(round(self.calculator.divide(row['Value 1'], row['Value 2']), 9), float(row['Result']))
            self.assertEqual(round(self.calculator.result, 9), float(row['Result']))

    def test_multiply(self):
        test_data = CsvReader('Tests/Data/UnitTestMultiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square(self):
        test_data = CsvReader('Tests/Data/UnitTestSquare.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_root(self):
        test_data = CsvReader('Tests/Data/UnitTestSquareRoot.csv').data
        for row in test_data:
            self.assertEqual(round(self.calculator.squareRoot(row['Value 1']), 8), round(float(row['Result']), 8))
            self.assertEqual(round(self.calculator.result, 8), round(float(row['Result']), 8))


if __name__ ==  '__main__':
    unittest.main()
