import numpy as np
import matplotlib.dates as mdates

class Data:

    def __init__(self, fileLocation):
        date,bid,ask = np.loadtxt(fileLocation, unpack=True, delimiter=',', converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})
        self.date = date
        self.bid = bid
        self.ask = ask

    def averageLine(self):
        return ((self.bid+self.ask)/2)