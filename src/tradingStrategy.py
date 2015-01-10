from src.data import Data
from src.patternFinder import PatternFinder
from src.patternStorer import PatternStorer


class TradingStrategy:

    def __init__(self, data):
        self.patternStorer = PatternStorer(data)
        self.patternFinder = PatternFinder(70, self.patternStorer)

    def executePatternRecognition(self):
        self.patternStorer.patternStorage(10, 10)
        self.patternStorer.currentPattern()
        self.patternFinder.patternRecognition(self.patternStorer.allPatterns, self.patternStorer.patternForRecognition)

data = Data('/Users/mbottjer/Documents/personalProjects/patternRecognition/data/GBPUSD1d.txt')
tradingStrategy = TradingStrategy(data)
tradingStrategy.executePatternRecognition()
