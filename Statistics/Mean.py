from Calculator.Addition import addition
from Calculator.Division import division

def mean(data):
    # throw exception for empty list
    if len(data) == 0:
        raise Exception('Can not have an empty list')

    value_counter = len(data)
    sum = 0
    for value in data:
        sum = addition(sum, value)
    return division(value_counter, sum)