from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics import SampleMean
from Statistics.GenerateRandom import GenerateRandom
from CsvReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []
    result = 0

    def __init__(self):
        #self.data = GenerateRandom.with_seed_integers_list(0, 10, 6, 2)
        super().__init__()

    def sample_mean(self, sample_size):
        self.result = mean(self.data, sample_size)
        return self.result

    def mean(self, data):
        self.data = data
        self.result = mean(self.data)
        return self.result

    def median(self):
        self.result = median(self.data)
        return self.result