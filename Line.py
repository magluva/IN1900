import unittest


class Line:
    '''
    Line class takes two positional parameters:
    p1 = touple (x, y). Point on a line
    p2 = touple (x, y). Another point on a line
    A line object has methods:
    Line.line() = Computes a and b from y = ax+b. Returns touple (a, b)
    Line.Value() = Computes a value on the line at point x
    '''

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def line(self):
        a = (self.p2[1] - self.p1[1]) / float(self.p2[0] - self.p1[0])
        b = self.p1[1] - (a * self.p1[0])
        return a, b

    def value(self, x):
        tmp = self.line()
        y = tmp[0] * x + tmp[1]
        return y


# Line unittest child class
class Test_line(unittest.TestCase):
    def setUp(self):
        self.test = Line((0, -1), (2, 4))

    def test_line(self):
        expected1 = (2.5, -1.0)
        computed1 = self.test.line()
        expected2 = 0.25
        computed2 = self.test.value(0.5)
        expected3 = 1.5
        computed3 = self.test.value(1.)
        self.assertSequenceEqual(computed1, expected1)
        self.assertEqual(computed2, expected2)
        self.assertEqual(computed3, expected3)
        # When the order in iterable objects does mot matter, AssertCountEqual can be used. (assertItemsEqual in 2.7)
        # The assertEqual function actually calls assertSequenceEqual if dealing with an iterable object,
        # but in my opinion, calling assertSequenceEqual explicitly makes the code more readable
        # and lets you know you are asserting a tuple/list.


if __name__ == '__main__':
    unittest.main(verbosity=2)
