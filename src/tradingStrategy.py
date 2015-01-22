from src.data import Data
from src.patternFinder import PatternFinder
from src.patternStorer import PatternStorer

# setup data
dataLengthToAnalyse = 37000
data = Data('/Users/mbottjer/Documents/personalProjects/patternRecognition/data/GBPUSD1d.txt')
avgLine = data.averageLine()

# initialise patternStorer and patternFinder
patternFinder = PatternFinder(70)

# loop through data, first analysing 100 data points

while dataLengthToAnalyse < data.dataLength():
    dataToBeAnalysed = avgLine[:dataLengthToAnalyse]

    patternStorer = PatternStorer(dataToBeAnalysed, avgLine)
    patternStorer.patternStorage(30, 30)
    patternStorer.currentPattern(30)

    patternFinder.patternRecognition(patternStorer)

    dataLengthToAnalyse += 1
