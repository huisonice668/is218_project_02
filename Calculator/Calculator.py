from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Square import square
from Calculator.SquareRoot import squareRoot
from Calculator.Division import division

class Calculator:

    result = 0

    def _init_(self):
        pass

    def add(self, x, y):
        self.result = addition(x, y)
        return self.result

    def minus(self, x, y):
        self.result = subtraction(x, y)
        return self.result

    def divide(self, x, y):
        self.result = division(x, y)
        return self.result

    def multiply(self, x, y):
        self.result = multiplication(x, y)
        return self.result

    def square(self, x):
        self.result = square(x)
        return self.result

    def squareRoot(self, x):
        self.result = squareRoot(x)
        return self.result
