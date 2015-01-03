import unittest
from data import Data
from patternRecogniser import PatternRecogniser


class PatternRecognitionTest(unittest.TestCase):
    def setUp(self):
        self.patterRecogniser = PatternRecogniser()
        self.data = Data('testData/testDataTwo.txt')

    def test_percentage_change(self):
        percentage = self.patterRecogniser.percentChange(2, 3)
        self.assertEquals(percentage, 50)

    def test_generation_of_patterns(self):
        avgLine = [1,2,3,4,5,6,7,8,9,10]
        pattern = []
        patternLength = 2
        startingPoint = 2
        self.patterRecogniser.generateIndividualPatterns(avgLine,pattern,patternLength,startingPoint)
        self.assertEquals(pattern, [100.0, 200.0])


if __name__ == '__main__':
    unittest.main()

