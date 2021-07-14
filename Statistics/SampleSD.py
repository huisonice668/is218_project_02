from Calculator.SquareRoot import squareRoot
from Statistics.SampleVar import sample_var

def sample_sd(data):
    #formula: sqrt(var)

    if len(data) == 0:
        raise ValueError('List can not be empty')

    var = sample_var(data)
    result = squareRoot(var)
    return result
