from src.Calculator import Calculator
from src.graphFX import GraphFX


class PatternFinder:

    def __init__(self, acceptedPercentageSimilarity):
        self.acceptedPercentageSimilarity = acceptedPercentageSimilarity
        self.calculate = Calculator()
        self.similarityOfPatterns = []

    def patternRecognition(self, storedPattern):
        for eachPattern in storedPattern.allPatterns:
            individualSimilarityPercentages = []
            self.createArrayOfSimilarities(eachPattern, storedPattern.patternForRecognition, individualSimilarityPercentages)
            similarity = self.calculate.averageOf(individualSimilarityPercentages)
            self.determinePatternsWithSimilarity(similarity, self.acceptedPercentageSimilarity, eachPattern, storedPattern)
            self.similarityOfPatterns.append(similarity)

    def createArrayOfSimilarities(self, pattern, currentPattern, individualSimilarityPercentages):
        for x in range(0,len(pattern)):
            individualSimilarityPercentages.append(100 - abs(self.calculate.percentChangeOf(pattern[x], currentPattern[x])))

    def determinePatternsWithSimilarity(self, similarity, percentage, pattern, storedPattern):
        if similarity > percentage:
            patternIndex = storedPattern.allPatterns.index(pattern)

            print "Pattern for recognition:"
            print storedPattern.patternForRecognition
            print "========================"
            print pattern
            print "------------------------"
            print "The predicted outcome is:"
            print storedPattern.outcomeArray[patternIndex]
            print "------------------------"
            graph = GraphFX()
            graph.plotPatternForRecognitionAgainstCurrentPattern(storedPattern.patternForRecognition, pattern)
