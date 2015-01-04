import unittest
import matplotlib.dates as mdates
import numpy as np
from src.data import Data


class DataTest(unittest.TestCase):

    def test_bid_ask_data_timestamp_is_converted_to_epoch(self):
        date,bid,ask = np.loadtxt('./testData/testData.txt', unpack=True, delimiter=',', converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})
        self.assertEquals(date, 734989.0)
        self.assertEquals(bid, 1.55358)
        self.assertEquals(ask, 1.55371)

    def test_average_line(self):
        data = Data('./testData/testData.txt')
        self.assertEquals(data.averageLine(), 1.5536449999999999)

if __name__ == '__main__':
    unittest.main()
