from Calculator.Addition import addition
from Calculator.Subtraction import subtraction

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


'''''''''
    def multiply(self, x, y):
        return multiplication(x, y)
        #return x * y

    def divide(self, x, y):
        return division(x, y)
        if y == 0:
            raise ValueError("Can not divide by zero")
        return x / y

    def square(self, x):
        return squaring(x)
       # return x * x

    def squareRoot(self, x):
        return squareRoots(x)
       # return math.sqrt(x)
'''''''''''

