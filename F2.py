
class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def __call__(self, x):
        import numpy as np
        return np.exp(-self.a*x)*np.sin(self.w*x)

    def __str__(self):
        return "exp(-a*x)*sin(w*x)"

# Terminal Output:
'''
See F2_shell.py or import and run the code.
'''
