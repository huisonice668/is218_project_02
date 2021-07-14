from Calculator.Calculator import Calculator
from Statistics import Mean
from Statistics import SampleMean
from CsvReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []
    result = 0

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def sample_mean(self, sample_size):
        self.result = mean(self.data, sample_size)
        return self.result

    def mean(self):
        self.result = mean(self.data)
        return self.result

    def median(self):
        self.result = median(self.data)
        return self.result