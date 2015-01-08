import time
from src.data import Data


class PatternStorer:

    # Pattern storer should have a constructor that takes a data object

    def __init__(self, data):
        self.avgLine = data.averageLine()

    allPatterns = []
    outcomeArray = []
    patternForRecognition = []

    def percentChange(self, startPoint, currentPoint):
        return ((float(currentPoint) - startPoint) / abs(startPoint))*100.00

    def generateIndividualPatterns(self, pattern, patternLength, startingPoint):
        oneLessPatternLength = patternLength - 1
        while oneLessPatternLength >= 0:
            pattern.append(self.percentChange(self.avgLine[startingPoint - patternLength],
                                              self.avgLine[startingPoint - oneLessPatternLength]))
            oneLessPatternLength -= 1

    def patternStorage(self, startingPoint, patternLength):
        usableData = len(self.avgLine) - 30
        patternStorageStartTime = time.time()

        while startingPoint < usableData:
            pattern = []

            self.generateIndividualPatterns(pattern, patternLength, startingPoint)

            outcomeRange = self.avgLine[startingPoint+20: startingPoint+30]
            currentPoint = self.avgLine[startingPoint]

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

    def currentPattern(self):
        for x in range(-10, 0):
            self.patternForRecognition.append(self.percentChange(self.avgLine[-11], self.avgLine[x]))
        print self.patternForRecognition

    def patternRecognition(self):
        similarityOfPatterns = []
        for eachPattern in self.allPatterns:
            individualSimilarityPercentages = []
            for x in range(0,10):
                individualSimilarityPercentages.append(100 - abs(self.percentChange(eachPattern[0], self.currentPattern()[0])))
            similarity = reduce(lambda x, y: x+y, individualSimilarityPercentages) / float(len(individualSimilarityPercentages))
            self.determinePattersWithSimilarity(similarity, 90, eachPattern)
            similarityOfPatterns.append(similarity)

    def determinePatternsWithSimilarity(self, similarity, percentage, pattern):
        if similarity > percentage:
            patternIndex = self.allPatterns.index(pattern)

        print "Pattern for recognition:"
        print self.patternForRecognition
        print "========================"
        print pattern
        print "The predicted outcome is" + self.outcomeArray[patternIndex]


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

data = Data('../data/GBPUSD1d.txt')
pR = PatternStorer(data)

pR.patternStorage(10, 10)
pR.currentPattern()