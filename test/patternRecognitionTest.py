import unittest
from data import Data
from patternRecogniser import PatternRecogniser


class PatternRecognitionTest(unittest.TestCase):

    def setUp(self):
        self.patterRecogniser = PatternRecogniser()
        self.data = Data('testData/testDataTwo.txt')

    def test_percentage_change(self):
        percentage = self.patterRecogniser.percentChange(2,3)
        self.assertEquals(percentage, 50)

    def test_pattern_storage(self):
        self.assertIsNotNone(self.patterRecogniser.patternFinder(6, self.data, 2))


if __name__ == '__main__':
    unittest.main()

