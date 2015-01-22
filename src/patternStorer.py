import time
from src.Calculator import Calculator
from src.data import Data


class PatternStorer:
    def __init__(self, data, totalAverageData):
        self.calculate = Calculator()
        self.data = data
        self.allPatterns = []
        self.outcomeArray = []
        self.patternForRecognition = []
        self.totalAverageData = totalAverageData

    def generateIndividualPatterns(self, pattern, patternLength, startingPoint):
        oneLessPatternLength = patternLength - 1
        while oneLessPatternLength >= 0:
            pattern.append(self.calculate.percentChangeOf(self.data[startingPoint - patternLength],
                                                        self.data[startingPoint - oneLessPatternLength]))
            oneLessPatternLength -= 1

    def patternStorage(self, startingPoint, patternLength):
        usableData = len(self.data) - 60
        # print usableData, "usable points"
        patternStorageStartTime = time.time()

        while startingPoint < usableData:
            pattern = []

            self.generateIndividualPatterns(pattern, patternLength, startingPoint)

            outcomeRange = self.data[startingPoint + 20: startingPoint + 30]
            currentPoint = self.data[startingPoint]

            futureOutcome = self.calculate.percentChangeOf(currentPoint, self.calculate.averageOf(outcomeRange))
            self.allPatterns.append(pattern)
            self.outcomeArray.append(futureOutcome)

            startingPoint += 1

        endTime = time.time()

        self.printPatternDetails(self.allPatterns, self.outcomeArray, patternStorageStartTime, endTime)

    def currentPattern(self, patternLength):
        for x in range(-(patternLength), 0):
            self.patternForRecognition.append(
                self.calculate.percentChangeOf(self.data[-(patternLength + 1)], self.data[x]))

    def printPatternDetails(self, allPatterns, outcomeArray, startTime, endTime):
        print len(allPatterns), "patterns"
        print len(outcomeArray), "outcomes"
        self.calculatePatternStorageTime(startTime, endTime)

    def calculatePatternStorageTime(self, startTime, endTime):
        print 'Pattern storage took:', endTime - startTime, 'seconds'