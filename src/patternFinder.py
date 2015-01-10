from src.Calculator import Calculator


class PatternFinder:

    def __init__(self, acceptedPercentageSimilarity, patternStorer):
        self.acceptedPercentageSimilarity = acceptedPercentageSimilarity
        self.calculate = Calculator()
        self.patternStorer = patternStorer

    def patternRecognition(self, allPatterns, currentPattern):
        similarityOfPatterns = []
        for eachPattern in allPatterns:
            individualSimilarityPercentages = []
            self.createArrayOfSimilarities(eachPattern, currentPattern, individualSimilarityPercentages)
            similarity = self.averagePointToPointSimilarities(individualSimilarityPercentages)
            self.determinePatternsWithSimilarity(similarity, self.acceptedPercentageSimilarity, eachPattern, allPatterns)
            similarityOfPatterns.append(similarity)

    def createArrayOfSimilarities(self, pattern, currentPattern, individualSimilarityPercentages):
        for x in range(0,10):
            individualSimilarityPercentages.append(100 - abs(self.calculate.percentChange(pattern[x], currentPattern[x])))

    def averagePointToPointSimilarities(self, arrayOfPercentages):
        similarity = reduce(lambda x, y: x+y, arrayOfPercentages) / len(arrayOfPercentages)
        return similarity

    def determinePatternsWithSimilarity(self, similarity, percentage, pattern, allPatterns):
        if similarity > percentage:
            patternIndex = allPatterns.index(pattern)

            print "Pattern for recognition:"
            print self.patternStorer.patternForRecognition
            print "========================"
            print pattern
            print "------------------------"
            print "The predicted outcome is:"
            print self.patternStorer.outcomeArray[patternIndex]
            print "------------------------"
