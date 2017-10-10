import unittest
from calculate import *
from fractions import Fraction


class testCalculate(unittest.TestCase):
    def testPrintfix(self):
        self.assertEqual(printFix([1, '+', 2, '*', 3]),
                         ['1', '+', '2', '*', '3', '='])
        self.assertEqual(
            printFix([3, '+', 4, '*', 5, '-', 7]), ['3', '+', '4', '*', '5', '-', '7', '='])

    def testPrior(self):
        self.assertEqual(Prior('*', '/'), False)
        self.assertEqual(Prior('*', '-'), True)

    def testChangetopostfix(self):
        self.assertEqual(changeToPostfix(
            [34, '+', 50, '-', 4, '*', 46]), [34, 50, '+', 4, 46, '*', '-'])
        self.assertEqual(changeToPostfix([54, '+', 53, '/', 35, '/', 66, '/', 17, '+', 19]), [
                         54, 53, 35, '/', 66, '/', 17, '/', '+', 19, '+'])

    def testCalculatepostfix(self):
        self.assertEqual(CalculatePostfix(
            [34, 50, '+', 4, 46, '*', '-']), -100)
        self.assertEqual(CalculatePostfix(
            [54, 53, 35, '/', 66, '/', 17, '/', '+', 19, '+']), Fraction(2866763, 39270))


if __name__ == '__main__':
    unittest.main()
