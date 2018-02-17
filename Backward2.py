import numpy as np

class Diff:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = h


class Backward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x)-f(x-h))/h


class Backward2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x-2*h)-(4*f(x-h))+3*f(x))/(2*h)


def g(t):
    return np.e**-t

def comparison_table(*args):
    # unpacking args
    b1, b2, h, t = args
    test_value = 0
    exact = -1*g(test_value)
    b1_error = abs(b1-exact)
    b2_error = abs(b2-exact)
    b1_vs_b2 = abs(b1_error-b2_error)
    # Display options contol flow
    print("Do you want to display table in standard format or decimal?");form = input("s/d:")
    # Formatted table
    print("{0:^30}".format("Backward1 - Backward2 comparison"))
    print("\n{0:^30}{1}{2:^30}".format("b1 error", "b2 error", " b1-b2 error diff"))
    print("----------------------------------------------------------------")
    if form.lower() == "s":
        [print("Result: {0:>14.5e}{1:>18.5e}{2:>20.5e}"\
        .format(i, ii, iii)) for i, ii, iii in zip(b1_error, b2_error, b1_vs_b2)]
    else:
        [print("Result: {0:>12.5f}{1:>20.5f}{2:>20.5f}"\
        .format(i, ii, iii)) for i, ii, iii in zip(b1_error, b2_error, b1_vs_b2)]
    print("----------------------------------------------------------------")
    print("Exact:{0:>11}".format(exact))
    print("----------------------------------------------------------------")

def main():
    # initializing h-array and t-array(only zeros for vectorized code)
    h = np.array([2**-k for k in range(15)])
    t = np.zeros(np.shape(h)[0])
    # Creating instances:
    obj1 = Backward1(g, h)
    b1 = obj1(t)
    obj2 = Backward2(g, h)
    b2 = obj2(t)
    # Calling table function
    comparison_table(b1, b2, h, t)

if __name__ == "__main__":
    main()

# Terminal Output:
'''
$ python Backward2.py
Do you want to display table in standard format or decimal?
s/d:s
Backward1 - Backward2 comparison

           b1 error           b2 error       b1-b2 error diff
----------------------------------------------------------------
Result:    7.18282e-01       7.57964e-01         3.96826e-02
Result:    2.97443e-01       1.23397e-01         1.74046e-01
Result:    1.36102e-01       2.52392e-02         1.10862e-01
Result:    6.51876e-02       5.72642e-03         5.94612e-02
Result:    3.19113e-02       1.36494e-03         3.05464e-02
Result:    1.57890e-02       3.33263e-04         1.54558e-02
Result:    7.85335e-03       8.23409e-05         7.77101e-03
Result:    3.91644e-03       2.04647e-05         3.89598e-03
Result:    1.95567e-03       5.10119e-06         1.95057e-03
Result:    9.77199e-04       1.27343e-06         9.75925e-04
Result:    4.88440e-04       3.18124e-07         4.88122e-04
Result:    2.44180e-04       7.95017e-08         2.44101e-04
Result:    1.22080e-04       1.98725e-08         1.22060e-04
Result:    6.10376e-05       4.96948e-09         6.10327e-05
Result:    3.05182e-05       1.23691e-09         3.05170e-05
----------------------------------------------------------------
Exact:       -1.0
----------------------------------------------------------------
'''
