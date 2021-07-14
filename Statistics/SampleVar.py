from Calculator.Square import square
from Calculator.Division import division
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean


def sample_var(data):
    # formula: (sum of (value x - mean) ^2 ) / (n - 1)

    if len(data) == 0:
        raise ValueError('List can not be empty')

    sample_mean = mean(data)

    sum_of_diff = 0
    for num in data:
        diff = subtraction(sample_mean, num)
        sqr_diff = square(diff)
        sum_of_diff = addition(sqr_diff, sum_of_diff)

    length = subtraction(1, len(data))
    result = division(length, sum_of_diff)

    return result
