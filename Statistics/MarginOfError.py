from Calculator.SquareRoot import squareRoot
from Calculator.Square import square
from Calculator.Division import division
from Calculator.Multiplication import multiplication
from Statistics.SampleSD import sample_sd


def margin_of_error(data, q):
    # formula: quantile * sqrt(sd ^2 / sample size)

    last_part = division(len(data), square(sample_sd(data)))
    last = squareRoot(last_part)
    result = multiplication(q, last)
    return result



