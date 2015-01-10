import time
from src.Calculator import Calculator
from src.data import Data

class PatternStorer:

    def __init__(self, data):
        self.calculate = Calculator()
        self.avgLine = data.averageLine()

    allPatterns = []
    outcomeArray = []
    patternForRecognition = []

    def generateIndividualPatterns(self, pattern, patternLength, startingPoint):
        oneLessPatternLength = patternLength - 1
        while oneLessPatternLength >= 0:
            pattern.append(self.calculate.percentChange(self.avgLine[startingPoint - patternLength],
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

            futureOutcome = self.calculate.percentChange(currentPoint, outcomeRange)
            self.allPatterns.append(pattern)
            self.outcomeArray.append(futureOutcome)

            startingPoint += 1

        endTime = time.time()

        self.printPatternDetails(self.allPatterns, self.outcomeArray, patternStorageStartTime, endTime)

    def currentPattern(self):
        for x in range(-10, 0):
            self.patternForRecognition.append(self.calculate.percentChange(self.avgLine[-11], self.avgLine[x]))

    # def patternRecognition(self, percentageSimilarity):
    #     similarityOfPatterns = []
    #     for eachPattern in self.allPatterns:
    #         individualSimilarityPercentages = []
    #         for x in range(0,10):
    #             individualSimilarityPercentages.append(100 - abs(self.calculate.percentChange(eachPattern[x], self.patternForRecognition[x])))
    #         similarity = reduce(lambda x, y: x+y, individualSimilarityPercentages) / len(individualSimilarityPercentages)
    #         self.determinePatternsWithSimilarity(similarity, percentageSimilarity, eachPattern)
    #         similarityOfPatterns.append(similarity)
    #
    # def determinePatternsWithSimilarity(self, similarity, percentage, pattern):
    #     if similarity > percentage:
    #         patternIndex = self.allPatterns.index(pattern)
    #
    #         print "Pattern for recognition:"
    #         print self.patternForRecognition
    #         print "========================"
    #         print pattern
    #         print "------------------------"
    #         print "The predicted outcome is:"
    #         print self.outcomeArray[patternIndex]
    #         print "------------------------"


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
        print 'Pattern storage took:', endTime - startTime, 'seconds'

# data = Data('../data/GBPUSD1d.txt')
# pR = PatternStorer(data)
#
# pR.patternStorage(10, 10)
# pR.currentPattern()