from src.Calculator import Calculator


class PatternFinder:

    def __init__(self):
        self.calculate = Calculator()

    def patternRecognition(self, percentageSimilarity, patterns):
        similarityOfPatterns = []
        for eachPattern in patterns:
            individualSimilarityPercentages = []
            for x in range(0,10):
                individualSimilarityPercentages.append(100 - abs(self.calculate.percentChange(eachPattern[x], self.patternForRecognition[x])))
            similarity = reduce(lambda x, y: x+y, individualSimilarityPercentages) / len(individualSimilarityPercentages)
            self.determinePatternsWithSimilarity(similarity, percentageSimilarity, eachPattern)
            similarityOfPatterns.append(similarity)

    def determinePatternsWithSimilarity(self, similarity, percentage, pattern):
        if similarity > percentage:
            patternIndex = self.allPatterns.index(pattern)

            print "Pattern for recognition:"
            print self.patternForRecognition
            print "========================"
            print pattern
            print "------------------------"
            print "The predicted outcome is:"
            print self.outcomeArray[patternIndex]
            print "------------------------"
