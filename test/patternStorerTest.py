import unittest

from src.data import Data
from src.patternStorer import PatternStorer


class PatternStoringTest(unittest.TestCase):
    def setUp(self):
        self.patternStorer = PatternStorer([1,2,4,8])
        self.patternStorerTwo = PatternStorer([1,2,3,4,5,6,7,8,9,10])

    def test_generation_of_patterns_works_by_tracking_movement_from_original_point(self):
        pattern = []
        patternLength = 2
        startingPoint = 2

        self.patternStorer.generateIndividualPatterns(pattern, patternLength, startingPoint)
        self.assertEquals(pattern, [100.0, 300.0])

    def test_current_pattern(self):
        self.patternStorerTwo.currentPattern(2)
        self.assertEquals(self.patternStorerTwo.patternForRecognition, [12.5, 25.0])

    def test_current_patten_when_provided_negative_value(self):
        self.patternStorerTwo.currentPattern(-2)
        self.assertEquals(self.patternStorerTwo.patternForRecognition, [])

    def test_pattern_storage(self):
        self.patternStorerTwo.patternStorage(2,2)
        self.assertEqual(self.patternStorerTwo.allPatterns, [1])


if __name__ == '__main__':
    unittest.main()

