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

    def dataLength(self):
        dataLength = int(self.bid.shape[0])
        # print 'data length is:', dataLength
        return dataLength