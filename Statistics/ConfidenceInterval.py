from Calculator.SquareRoot import squareRoot
from Calculator.Division import division
from Calculator.Multiplication import multiplication
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean
from Statistics.SampleSD import sample_sd


def confidence_interval(data, level):
    # formula: sample mean +- (level * sd) / sqrt(size n)

    if len(data) == 0:
        raise ValueError('List can not be empty')

    mean_value = mean(data)
    print(mean_value)

    sd = sample_sd(data)
    print('sd = ', sd)


    lower_bound = 0
    higher_bound = 0
    sqrt_size = squareRoot(len(data))

    last_part = division(sqrt_size, (multiplication(level, sd)))
    lower_bound = subtraction(last_part,mean_value)
    higher_bound = addition(last_part, mean_value)

    return lower_bound
