from src.data import Data
from src.patternFinder import PatternFinder
from src.patternStorer import PatternStorer


class TradingStrategy():

    def __init__(self):
        self.data = Data('../data/GBPUSD1d.txt')
        self.patternStorer = PatternStorer(self.data)
        self.patternFinder = PatternFinder()


