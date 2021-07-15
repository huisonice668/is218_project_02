from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.SampleMean import sample_mean
from Statistics.SampleSD import sample_sd
from Statistics.SampleVar import sample_var
from Statistics.ConfidenceInterval import confidence_interval
from Statistics.MarginOfError import margin_of_error

from Statistics import SampleMean
from Statistics.GenerateRandom import GenerateRandom
from CsvReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []
    result = 0
    modeHelper = 0

    def __init__(self):
        #self.data = GenerateRandom.with_seed_integers_list(0, 10, 6, 2)
        super().__init__()

    def mean(self, data):
        self.data = data
        self.result = mean(self.data)
        return self.result

    def median(self, data):
        self.data = data
        self.result = median(self.data)
        return self.result

    def mode(self, data):
        self.data = data
        self.result = mode(self.data)
        return self.result

    def sample_var(self, data):
        self.result = sample_var(data)
        return self.result


    def sample_sd(self, data):
        self.result = sample_sd(data)
        return self.result


    def confidence_interval(self, data, level):
        self.result = confidence_interval(data, level)
        return self.result

    def margin_of_error(self, data, q):
        self.result = margin_of_error(data, q)
        return self.result


    def sample_mean(self, data, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result


