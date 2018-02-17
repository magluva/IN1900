
# Defining roots function()
def roots(a, b, c):
    from numpy.lib.scimath import sqrt as csqrt
    r1 = (-b - csqrt((b**2) - (4 * a * c))) / (2 * a)
    r2 = (-b + csqrt((b**2) - (4 * a * c))) / (2 * a)
    return r1, r2

# Defining test_float_function()
def test_roots_float():
    a = 2; b = 5; c = -3
    expected = (-3., 0.5)
    calculated = roots(a, b, c)
    tol = 1E-14
    # Calculating success for roots vs. expected
    success_r1 = (abs(calculated[0] - expected[0]) < tol)
    success_r2 = (abs(calculated[1] - expected[1]) < tol)
    # Using if/else statement for feedback purposes. Assert also an option.
    if((success_r1 and success_r2) == True):
        print("Test_float: Passed!")
    else:
        print("Test_float: Failed!")
    return

# Defining test_complex_function()
def test_roots_complex():
    a = 1; b = 3; c = 3
    expected = (-1.5 - 0.86602540378444j, -1.5 + 0.86602540378444j)
    calculated = roots(a, b, c)
    tol = 1E-14
    # Calculating success for roots vs. expected.
    success_r1 = (abs(calculated[0] - expected[0]) < tol)
    success_r2 = (abs(calculated[1] - expected[1]) < tol)
    # Using if/else statement for feedback purposes. Assert also an option.
    if((success_r1 and success_r2) == True):
        print("Test_complex: Passed!")
    else:
        print("Test_complex: Failed!")
    return

def main():

    # Output:
    # Result of roots() on known values to screen.
    print("Float:   {}".format(roots(2, 5, -3)))
    print("Complex:   {}".format(roots(1, 3, 3)))
    print("")
    # Calling test functions()
    test_roots_float()
    test_roots_complex()

if __name__ == '__main__':
    main()

# Terminal Output:
'''
$ python roots_quadratic.py
Float:   (-3.0, 0.5)
Complex:   ((-1.5-0.8660254037844386j), (-1.5+0.8660254037844386j))

Test_float: Passed!
Test_complex: Passed!

'''
