
# All global variables are stored in ir_const.py
# and imported as constants due to scalability
# and it makes them easier to find/change.
# If you want me to keep all variables and "constants" in the main file,
# let me know via the feedback:)

# Fetching "constants" (need not assign to var)
from gauss1_const import M, S, X
# Importing necessary functions from math module
from math import sqrt, exp, pi

# Function calculating the gaussian expression
def gauss1(m, s, x):
    ans = (1 / (sqrt(2 * pi) * s)) * exp((-1/2) * ((x - m)/s)**2)
    return ans

# Test function with timin capabilities and localized variables
def test_calc():
    import timeit
    m, s, x = 0, 2, 1
    expected = 0.17603266338214
    result = gauss1(m, s, x)
    tol = 1E-14
    success = abs(expected - result) < tol
    t = timeit.Timer(stmt="(gaussian1.gauss1(gaussian1.M, gaussian1.S, gaussian1.X))", setup="import gaussian1")
    if(success):
        return "\nTest passed!\nTime elapsed: {} seconds".format(t.timeit(number=1))
    else:
        return "Test failed!"

def main():

    # Function calls
    out = gauss1(M, S, X)
    test = test_calc()

    # Output
    print("\nResults:")
    print("gauss1(m,s,x): {}".format(out))
    print(test)


if __name__ == '__main__':
    main()

# Terminal Output:
'''
$ python gaussian1.py

Results:
gauss1(m,s,x): 0.17603266338214976

Test passed!
Time elapsed: 4.94800042361021e-06 seconds
'''
