class Calculator:

    def percentChangeOf(self, startPoint, currentPoint):
        try:
            x = ((float(currentPoint) - startPoint) / abs(startPoint))*100.00
            if x == 0.0:
                return 0.000000000001
            else:
                return x
        except:
            return 0.000000000001

    def averageOf(self, array):
        try:
            return reduce(lambda pointOne, pointTwo: pointOne + pointTwo, array) / len(array)
        except Exception as e:
            print str(e)
            return 0