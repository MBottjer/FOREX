from src.Calculator import Calculator
from src.graphFX import GraphFX


class PatternFinder:

    def __init__(self, acceptedPercentageSimilarity):
        self.acceptedPercentageSimilarity = acceptedPercentageSimilarity
        self.calculate = Calculator()
        self.allPatternsRecognised = []
        self.similarityOfPatterns = []
        self.patternFound = False
        self.predictedOutcomeArray = []

    def patternRecognition(self, storedPattern):
        for eachPattern in storedPattern.allPatterns:
            individualSimilarityPercentages = []
            self.createArrayOfSimilarities(eachPattern, storedPattern.patternForRecognition, individualSimilarityPercentages)
            similarity = self.calculate.averageOf(individualSimilarityPercentages)
            self.determinePatternsWithSimilarity(similarity, self.acceptedPercentageSimilarity, eachPattern, storedPattern)
            self.similarityOfPatterns.append(similarity)
        if self.patternFound:
            graph = GraphFX()
            graph.plotAllPatternsAgainstCurrentPattern(storedPattern, self.allPatternsRecognised, self.predictedOutcomeArray)

    #create array of patterns with length 30
    def createArrayOfSimilarities(self, pattern, currentPattern, individualSimilarityPercentages):
        for x in range(0,len(pattern)):
            individualSimilarityPercentages.append(100 - abs(self.calculate.percentChangeOf(pattern[x], currentPattern[x])))

    def determinePatternsWithSimilarity(self, similarity, percentage, pattern, storedPattern):
        if similarity > percentage:
            patternIndex = storedPattern.allPatterns.index(pattern)
            self.patFound = 1
            self.allPatternsRecognised.append(pattern)
            self.patternFound = True
            self.printPatternFoundDetails(storedPattern, pattern, patternIndex)
            # graph = GraphFX()
            # graph.plotPatternForRecognitionAgainstCurrentPattern(storedPattern.patternForRecognition, pattern)


    def printPatternFoundDetails(self, storedPattern, pattern, patternIndex):
        print "Pattern for recognition:"
        print storedPattern.patternForRecognition
        print "========================"
        print pattern
        print "------------------------"
        print "The predicted outcome is:"
        print storedPattern.outcomeArray[patternIndex]
        print "------------------------"