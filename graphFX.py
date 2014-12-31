import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from data import Data


class GraphFX:

    def graphRawFX(self):

        data = Data('data/GBPUSD1d.txt')

        figure = plt.figure(figsize=(10,7))
        axisOne = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)

        axisOne.plot(data.date,data.bid)
        axisOne.plot(data.date,data.ask)
        plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

        axisOne.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

        for label in axisOne.xaxis.get_ticklabels():
            label.set_rotation(45)

        axisOneSpread = axisOne.twinx()
        axisOneSpread.fill_between(data.date, 0, (data.ask-data.bid), facecolor='g', alpha=.3)

        plt.subplots_adjust(bottom=.23)

        plt.grid(True)
        plt.show()

graph = GraphFX()

graph.graphRawFX()