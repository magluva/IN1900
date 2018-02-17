# Using super() instead of explicit super class call
import numpy as np

class Line:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
        print("Line.__call__() was  called ... END OF CYCLE\n")
        return self.c0+self.c1*x

    def table(self, L, R, n):
        s = ""
        h = "\n{0:^12s}{1:^12s}\n".format("x", "y")
        for x in np.linspace(L, R, n):
            y = self(x)
            s += "{0:^12g}{1:^12g}\n".format(x, y)
        return h+s


class Parabola(Line):
    def __init__(self, c0, c1, c2):
        super(Parabola, self).__init__(c0, c1)
        self.c2 = c2

    def __call__(self, x):
        print("Parabola.__call__() was  called ...")
        return super(Parabola, self).__call__(x)+self.c2*x**2


class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        super(Cubic, self).__init__(c0, c1, c2)
        self.c3 = c3

    def __call__(self, x):
        print("Cubic.__call__() was  called ...")
        return super(Cubic, self).__call__(x) + self.c3*x**3


class Poly(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        super(Poly, self).__init__(c0, c1, c2, c3)
        self.c4 = c4

    def __call__(self, x):
        print("Poly.__call__() was  called ...")
        return super(Poly, self).__call__(x) + self.c4*x**4

def main():
    # Creating Poly class instance
    p = Poly(1, 2, 3, 4, 5)
    # print new line + table
    # This will display n=7 __call__ cycles
    print("")
    print(p.table(0, 6, 7))

if __name__ == "__main__":
    main()

# Terminal Output:
'''
$ python Cubic_Poly4.py

Poly.__call__() was  called ...
Cubic.__call__() was  called ...
Parabola.__call__() was  called ...
Line.__call__() was  called ... END OF CYCLE

Poly.__call__() was  called ...
Cubic.__call__() was  called ...
Parabola.__call__() was  called ...
Line.__call__() was  called ... END OF CYCLE

Poly.__call__() was  called ...
Cubic.__call__() was  called ...
Parabola.__call__() was  called ...
Line.__call__() was  called ... END OF CYCLE

Poly.__call__() was  called ...
Cubic.__call__() was  called ...
Parabola.__call__() was  called ...
Line.__call__() was  called ... END OF CYCLE

Poly.__call__() was  called ...
Cubic.__call__() was  called ...
Parabola.__call__() was  called ...
Line.__call__() was  called ... END OF CYCLE

Poly.__call__() was  called ...
Cubic.__call__() was  called ...
Parabola.__call__() was  called ...
Line.__call__() was  called ... END OF CYCLE

Poly.__call__() was  called ...
Cubic.__call__() was  called ...
Parabola.__call__() was  called ...
Line.__call__() was  called ... END OF CYCLE


     x           y
     0           1
     1           15
     2          129
     3          547
     4          1593
     5          3711
     6          7465


̈́'''
