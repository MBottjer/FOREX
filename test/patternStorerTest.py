import unittest

from src.data import Data
from src.patternStorer import PatternStorer


class PatternStoringTest(unittest.TestCase):
    def setUp(self):
        self.patternStorer = PatternStorer()
        self.data = Data('testData/testDataTwo.txt')

    def test_generation_of_patterns(self):
        avgLine = [1,2,3,4,5,6,7,8,9,10]
        pattern = []
        patternLength = 2
        startingPoint = 2
        self.patternStorer.generateIndividualPatterns(avgLine,pattern,patternLength,startingPoint)
        self.assertEquals(pattern, [100.0, 200.0])

    def test_patter_finder(self):



if __name__ == '__main__':
    unittest.main()

