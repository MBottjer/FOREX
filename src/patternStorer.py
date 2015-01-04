import time
from src.data import Data


class PatternStorer:

    allPatterns = []
    outcomeArray = []

    def percentChange(self, startPoint, currentPoint):
        return ((float(currentPoint) - startPoint) / abs(startPoint))*100.00

    def generateIndividualPatterns(self, avgLine, pattern, patternLength, startingPoint):
        oneLessPatternLength = patternLength - 1
        while oneLessPatternLength >= 0:
            pattern.append(self.percentChange(avgLine[startingPoint - patternLength],
                                              avgLine[startingPoint - oneLessPatternLength]))
            oneLessPatternLength -= 1

    def patternStorage(self, startingPoint, patternLength, data):
        avgLine = data.averageLine()
        usableData = len(avgLine) - 30
        patternStorageStartTime = time.time()

        while startingPoint < usableData:
            pattern = []

            self.generateIndividualPatterns(avgLine, pattern, patternLength, startingPoint)

            outcomeRange = avgLine[startingPoint+20: startingPoint+30]
            currentPoint = avgLine[startingPoint]

            # self.printOutcomeComparison(outcomeRange, currentPoint, pattern)
            try:
                outcomeRange = reduce(lambda pointOne, pointTwo: pointOne+pointTwo, outcomeRange) / len(outcomeRange)
            except Exception as e:
                print str(e)
                avgOutcome = 0

            futureOutcome = self.percentChange(currentPoint, outcomeRange)
            self.allPatterns.append(pattern)
            self.outcomeArray.append(futureOutcome)

            startingPoint += 1

        endTime = time.time()

        self.printPatternDetails(self.allPatterns, self.outcomeArray, patternStorageStartTime, endTime)

    # def patternRecognition(self):
    #     patternForRecognition = []
    #
    #     for x in range(-10, -1):
    #         patternForRecognition.append(self.percentChange(av))

    def printPatternDetails(self, allPatterns, outcomeArray, startTime, endTime):
        print len(allPatterns)
        print len(outcomeArray)
        self.calculatePatternStorageTime(startTime, endTime)

    def printOutcomeComparison(self, outcomeRange, currentPoint, pattern):
        print reduce(lambda pointOne, pointTwo: pointOne+pointTwo, outcomeRange) / len(outcomeRange)
        print currentPoint
        print '______'
        print pattern
        print self.allPattern

    def calculatePatternStorageTime(self, startTime, endTime):
        print 'Patter storage took:', endTime - startTime, 'seconds'

pR = PatternStorer()
data = Data('../data/GBPUSD1d.txt')

pR.patternStorage(10, 10, data)