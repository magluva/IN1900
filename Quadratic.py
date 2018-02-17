import unittest


# Quadratic class
class Quadratic:
    '''
    This class takes positional parameters: a, b and c.
    A Quadratic object has methods:
    Quadratic.value() = calculate the value of x, returns float
    Quadratic.table() = Display x values in a range
    Quadratic.roots() = Calculate r1 and r2 from the equation ax²+ax+b=0
    '''

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def value(self, x):
        return (self.a*x**2)+(self.b*x)+self.c

    def table(self, L, R, n=20):
        import numpy as np
        interval = np.linspace(L, R, n)
        print("{0:<5} {1:<5}".format("x", "f(x)"))
        [print("{0:<5} {1:<5}".format(i, self.value(i))) for i in interval]


    def roots(self):
        from numpy.lib.scimath import sqrt as csqrt
        r1 = (-self.b - csqrt((self.b**2) - (4 * self.a * self.c))) / (2 * self.a)
        r2 = (-self.b + csqrt((self.b**2) - (4 * self.a * self.c))) / (2 * self.a)
        return r1, r2

# Quadratic unittest child class
class Test_quadratic(unittest.TestCase):
    # Unittest implementation with class Quadratic instance.
    def setUp(self):
        self.test = Quadratic(1, 3, 3)

    def test_triangle_area(self):
        expected = 133.
        calculated = self.test.value(10)
        self.assertEqual(calculated, expected)

    def test_triangle_perimeter(self):
        expected = (-1.5 - 0.8660254037844386j, -1.5 + 0.8660254037844386j)
        calculated = self.test.roots()
        self.assertEqual(calculated, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

# Terminal Output:
'''
 python Quadratic.py
test_triangle_area (__main__.Test_quadratic) ... ok
test_triangle_perimeter (__main__.Test_quadratic) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.045s

OK
'''
