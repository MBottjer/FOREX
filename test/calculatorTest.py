import unittest
from src.Calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()


    def test_average_of_array(self):
        average = self.calculator.averageOf([1,3,3,4,5,8])
        self.assertEquals(average, 4)

    def test_average_of_array_with_empty_array(self):
        average = self.calculator.averageOf([])
        self.assertEquals(average, 0)

    def test_percentage_change(self):
        percentage = self.calculator.percentChangeOf(2, 3)
        self.assertEquals(percentage, 50)

    def test_percentage_change_with_empty_array(self):
        percentage = self.calculator.percentChangeOf(0,0)
        self.assertEquals(percentage, 1e-12)

    def test_percentage_change_with_negative_values(self):
        percentageOne, percentageTwo = self.calculator.percentChangeOf(-10,10), self.calculator.percentChangeOf(10,-10)
        self.assertEquals(percentageOne, 200.00)
        self.assertEquals(percentageTwo, -200.00)

if __name__ == '__main__':
    unittest.main()