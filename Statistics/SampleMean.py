from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.GetSample import getSample
from Statistics.Mean import mean

def sample_mean(data, sample_size):
    sum = 0

    # check that sample size is not 0
    if sample_size == 0:
        raise Exception('Sample size can not be zero')

    # check that sample size is not larger than population size
    if sample_size > len(data):
        raise Exception('Sample size can not be greater than population size')

    sample = getSample(data, sample_size)
    value_counter = len(sample)

    # check that get sample returns the proper number of samples
    if sample_size != value_counter:
        raise Exception('Sample did not return proper number of samples')


    return mean(sample)
'''''''''
    for num in sample:
        sum = addition(sum, num)
    return division(value_counter, sum)
'''''''''

