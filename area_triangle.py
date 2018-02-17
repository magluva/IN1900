import unittest

class Triangle:
    # defining init-function() --constructor-like method
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    # Defining vertices method()
    def vertices(self):
        '''
        Makes list of vertices from vertex coordinates.
        '''
        return [self.v1, self.v2, self.v3]


    # Defining triangle_area method()
    def triangle_area(self, vertices):
        '''
        Calculates the area of triangle with vertex coordinates
        (0, 0), (1, 0), (0, 2).
        '''
        # There are multipple ways of implementing this, but i think
        # this is readable.
        A = ((1/2) * abs(vertices[1][0] * vertices[2][1] - \
                         vertices[2][0] * vertices[1][1] - \
                         vertices[0][0] * vertices[2][1] - \
                         vertices[2][0] * vertices[0][1] - \
                         vertices[0][0] * vertices[1][1] - \
                         vertices[1][0] * vertices[0][1]))
        return A

    # Defining test method()
    def test_triangle_area(self):
        '''
        Verify the area of triangle with vertex coordinates
        (0, 0), (1, 0), (0, 2).
        '''
        calc_vert = self.vertices()
        computed = self.triangle_area(calc_vert)
        expected = 1
        tol = 1E-14
        success = abs(computed - expected) < tol
        msg = "computed area = {} != {} (expected)".format(computed, expected)
        assert success, msg


class Test_triangle(unittest.TestCase):
    # Unittest implementation with class Triangle instance.

    def setUp(self):
        self.test = Triangle((0, 0), (1, 0), (0, 2))

    def test_vertices(self):
        self.assertEqual(self.test.vertices(), [(0, 0), (1, 0), (0, 2)])

    def test_triangle_area(self):
        expected = 1.
        calculated = self.test.triangle_area(self.test.vertices())
        self.assertEqual(calculated, expected)


def main():
    # Defininge variables as touples.
    v1 = (0, 0); v2 = (1, 0); v3 = (0, 2)
    # Initializing class Triangle.
    t = Triangle(v1, v2, v3)
    # Calling vertices() inside triangle_area() method
    A = t.triangle_area(t.vertices())
    # Output
    print("My calculated values from vertices {} {} and {} = {}\n".format(\
          v1, v2, v3, A))
    print("----------------------------------------------------------------------")
    # Calling test function()
    t.test_triangle_area()
    print("Self defined test function ran ... ok\n")
    print("----------------------------------------------------------------------")
    # Calling unitest on main()
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
    # It is common to put the unittest.main() call
    # here, in a test class module, but in this
    # case we want to run both main() and unittest.main().

# Terminal Output Success:
'''
$ python area_triangle.py
My calculated values from vertices (0, 0) (1, 0) and (0, 2) = 1.0

----------------------------------------------------------------------
Self defined test function ran ... ok

----------------------------------------------------------------------
test_triangle_area (__main__.Test_triangle) ... ok
test_vertices (__main__.Test_triangle) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
'''
# Terminal Output Test_triangle_area() Faile Example:
'''
$ python arpython area_triangle.py
My calculated values from vertices (0, 0) (1, 0) and (0, 2) = 1.0

----------------------------------------------------------------------
Traceback (most recent call last):
  File "area_triangle.py", line 66, in <module>
    main()
  File "area_triangle.py", line 60, in main
    t.test_triangle_area()
  File "area_triangle.py", line 32, in test_triangle_area
    assert success, msg
AssertionError: computed area = 1.0 != 2 (expected)
'''
