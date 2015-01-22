import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from py2app.recipes import numpy
from src.Calculator import Calculator

from src.data import Data


class GraphFX:

    def __init__(self):
        self.calculate = Calculator()

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

    def plotPatternForRecognitionAgainstCurrentPattern(self, patternForRecognition, eachPattern):
        xAxis = range(1,31)
        fig = plt.figure()
        plt.plot(xAxis, patternForRecognition)
        plt.plot(xAxis, eachPattern)
        # plt.show()

    def plotAllPatternsAgainstCurrentPattern(self, storedPattern, patternsToBePlotted, predictedOutcomeArray):
        fig = plt.figure(figsize=(10,6))
        xAxis = range(1,31)

        for eachPatt in patternsToBePlotted:
            futurePoints = storedPattern.allPatterns.index(eachPatt)

            if storedPattern.outcomeArray[futurePoints] > storedPattern.patternForRecognition[29]:
                pcolor = '#24bc00'
            else:
                pcolor = '#d40000'

            plt.plot(xAxis, eachPatt)
            predictedOutcomeArray.append(storedPattern.outcomeArray[futurePoints])

            plt.scatter(35, storedPattern.outcomeArray[futurePoints], c=pcolor, alpha=.3 )

        realOutcomeRange = storedPattern.totalAverageData[len(storedPattern.data)+20:len(storedPattern.data)+30]
        realAverageOutcome = self.calculate.averageOf(realOutcomeRange)
        realMovement = self.calculate.percentChangeOf(storedPattern.totalAverageData[len(storedPattern.data)], realAverageOutcome)
        predictedAverageOutcome = self.calculate.averageOf(predictedOutcomeArray)

        #Only a visual representation, not to scale (should be further away)
        plt.scatter(40, realMovement, c='#000000', s=25)

        plt.scatter(40, predictedAverageOutcome, c='#FF0000', s=25)


        plt.plot(xAxis, storedPattern.patternForRecognition, '#000000', linewidth = 3)
        plt.grid(True)
        plt.title('Pattern Recognition')
        plt.show()