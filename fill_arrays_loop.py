import numpy as np

# Setting variables as global to use in next assignment.
# (not good practice in large programs)
xmin = -4.
xmax = 4.
n = 41
dt = (xmax-xmin)/(n-1)

def h(x):
    # Simple h(x) function for calculating y-values
    return (1/np.sqrt(2 * np.pi)) * np.exp(-0.5*(x**2))

def main():
    # Since we in the next task are asked to use numpy.linspace
    # I will try to do it without it in this assignment.
    # range does not allow float, even as step, so i'll make my own.
    def equallity_for_floats(xmin, xmax, step):
        # xmax+1E-10 because of rounding errors
        while xmin < xmax+1E-10:
            yield xmin
            xmin += step

    # Creating two uninitialized arrays
    x = np.empty(n)
    y = np.empty(n)

    # Output
    print("{0:>10s} {1:>10s}".format("x", "h(x)"))
    for idx, val in enumerate(equallity_for_floats(xmin,xmax, dt)):
        # Initializing x and y arrays
        x[idx] = val
        y[idx] = h(val)
        # Output
        print("{0:>10.1f} {1:>10.4f}".format(x[idx], y[idx]))
    # The for loop cluld have been done in different ways. I used a custom generator
    # with enumerate() that i haven't timed.
if __name__ == '__main__':
    main()

# Terminal Output:
'''
$ python fill_arrays_loop.py
         x       h(x)
      -4.0     0.0001
      -3.8     0.0003
      -3.6     0.0006
      -3.4     0.0012
      -3.2     0.0024
      -3.0     0.0044
      -2.8     0.0079
      -2.6     0.0136
      -2.4     0.0224
      -2.2     0.0355
      -2.0     0.0540
      -1.8     0.0790
      -1.6     0.1109
      -1.4     0.1497
      -1.2     0.1942
      -1.0     0.2420
      -0.8     0.2897
      -0.6     0.3332
      -0.4     0.3683
      -0.2     0.3910
       0.0     0.3989
       0.2     0.3910
       0.4     0.3683
       0.6     0.3332
       0.8     0.2897
       1.0     0.2420
       1.2     0.1942
       1.4     0.1497
       1.6     0.1109
       1.8     0.0790
       2.0     0.0540
       2.2     0.0355
       2.4     0.0224
       2.6     0.0136
       2.8     0.0079
       3.0     0.0044
       3.2     0.0024
       3.4     0.0012
       3.6     0.0006
       3.8     0.0003
       4.0     0.0001
'''
