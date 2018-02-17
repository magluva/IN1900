import unittest
import numpy as np


# Rectangle class.
class Rectangle:
    '''
    This class takes positional arguments:
    h = height of rectangle
    w = width of rectangle
    xy = touple of x0, y0 coordinates
    A Rectangle object has the methods:
    Rectangle.area() = returns (float) area of the object
    Rectangle.perimeter() = returns (float) perimeter of object
    '''

    def __init__(self, w, h, xy):
        self.w = w
        self.h = h
        self.x0 = xy[0]
        self.y0 = xy[1]

    # Defining rectangle area method: return float
    def area(self):
        return self.h*self.w

    # Defining rectangle perimeter method: return float
    def perimeter(self):
        return 2*(self.h+self.w)


# Triangle class
class Triangle:
    '''
    This class takes positional arguments:
    v1 = touple of x0, y0 coordinates
    v2 = touple of x1, y1 coordinates
    v3 = touple of x2, y2 coordinates
    A Triangle object has the methods:
    Triangle.area() = returns (float) area of the object
    Triangle.perimeter() = returns (float) perimeter of object
    '''

    # defining init-function: constructor-like method
    def __init__(self, v1, v2, v3):
        self.v = [v1, v2, v3]

    # Defining triangle_area method return float
    def area(self):
        a = ((1/2) * abs(self.v[1][0] * self.v[2][1] - \
                         self.v[2][0] * self.v[1][1] - \
                         self.v[0][0] * self.v[2][1] - \
                         self.v[2][0] * self.v[0][1] - \
                         self.v[0][0] * self.v[1][1] - \
                         self.v[1][0] * self.v[0][1]))
        return a

    # Defining triangle perimeter method: return float
    def perimeter(self):
        p = np.sqrt(((self.v[0][1] - self.v[0][0])**2) + \
                    ((self.v[1][1] - self.v[1][0])**2)) + \
            np.sqrt(((self.v[1][1] - self.v[1][0])**2) + \
                    ((self.v[2][1] - self.v[2][0])**2)) + \
            np.sqrt(((self.v[2][1] - self.v[2][0])**2) + \
                    ((self.v[0][1] - self.v[0][0])**2))
        return p


# Rectangle unittest child class
class Test_rectangle(unittest.TestCase):
    def setUp(self):
        self.test = Rectangle(3, 5, (0, 0))

    def test_rectangle_area(self):
        expected = 15.
        calculated = self.test.area()
        self.assertEqual(calculated, expected)

    def test_rectangle_perimeter(self):
        expected = 16.
        calculated = self.test.perimeter()
        self.assertEqual(calculated, expected)


# Triangle unittest child class
class Test_triangle(unittest.TestCase):

    def setUp(self):
        self.test = Triangle((0, 0), (1, 0), (0, 2))

    def test_triangle_area(self):
        expected = 1.
        calculated = self.test.area()
        self.assertEqual(calculated, expected)

    def test_triangle_perimeter(self):
        expected = 5.2360679774997898
        calculated = self.test.perimeter()
        self.assertEqual(calculated, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

# Terminal Output:
'''
$ python geometric_shapes.py
test_rectangle_area (__main__.Test_rectangle) ... ok
test_rectangle_perimeter (__main__.Test_rectangle) ... ok
test_triangle_area (__main__.Test_triangle) ... ok
test_triangle_perimeter (__main__.Test_triangle) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
'''
