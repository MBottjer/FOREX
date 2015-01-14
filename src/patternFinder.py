from src.Calculator import Calculator
from src.graphFX import GraphFX


class PatternFinder:

    def __init__(self, acceptedPercentageSimilarity):
        self.acceptedPercentageSimilarity = acceptedPercentageSimilarity
        self.calculate = Calculator()

    def patternRecognition(self, storedPattern):
        similarityOfPatterns = []
        for eachPattern in storedPattern.allPatterns:
            individualSimilarityPercentages = []
            self.createArrayOfSimilarities(eachPattern, storedPattern.patternForRecognition, individualSimilarityPercentages)
            similarity = self.averagePointToPointSimilarities(individualSimilarityPercentages)
            self.determinePatternsWithSimilarity(similarity, self.acceptedPercentageSimilarity, eachPattern, storedPattern)
            similarityOfPatterns.append(similarity)

    def createArrayOfSimilarities(self, pattern, currentPattern, individualSimilarityPercentages):
        for x in range(0,len(pattern)):
            individualSimilarityPercentages.append(100 - abs(self.calculate.percentChangeOf(pattern[x], currentPattern[x])))

    def averagePointToPointSimilarities(self, arrayOfPercentages):
        return reduce(lambda x, y: x+y, arrayOfPercentages) / len(arrayOfPercentages)

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
