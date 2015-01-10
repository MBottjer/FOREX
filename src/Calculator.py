class Calculator:

    def percentChange(self, startPoint, currentPoint):
        try:
            x = ((float(currentPoint) - startPoint) / abs(startPoint))*100.00
            if x == 0.0:
                return 0.000000000001
            else:
                return x
        except:
            return 0.000000000001