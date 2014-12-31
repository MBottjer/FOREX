import time
from data import Data


class PatternRecogniser:

    def percentChange(self, startPoint, currentPoint):
        return ((float(currentPoint) - startPoint) / startPoint)*100

    def patternFinder(self, startingPoint, patternLength, data):
        avgLine = data.averageLine(data.bid, data.ask)
        usableData = len(avgLine) - 30

        while startingPoint < usableData:
            pattern = []
            twoLessPatternLength = patternLength - 2

            while twoLessPatternLength >= 0:
                pattern.append(self.percentChange(avgLine[startingPoint - patternLength], avgLine[startingPoint - twoLessPatternLength]))
                twoLessPatternLength -= 1

            outcomeRange = avgLine[startingPoint+20: startingPoint+30]
            currentPoint = avgLine[startingPoint]

            self.printOutcomeComparison(outcomeRange, currentPoint, pattern)

            startingPoint += 1

    def printOutcomeComparison(self, outcomeRange, currentPoint, pattern):
        print reduce(lambda pointOne, pointTwo: pointOne+pointTwo, outcomeRange) / len(outcomeRange)
        print currentPoint
        print '______'
        print pattern
        time.sleep(5)

pR = PatternRecogniser()
data = Data('data/GBPUSD1d.txt')

pR.patternFinder(10, 10, data)