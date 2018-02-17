# Code written as seen in exercise 7.11

from F2 import F
f = F(a=1.0, w=0.1)
from math import pi
print(f(x=pi))
f.a = 2
print(f(pi))
print(f)

# Terminal Output:
'''
$ python F2_shell.py
0.013353835137
0.00057707154012
exp(-a*x)*sin(w*x)
'''
