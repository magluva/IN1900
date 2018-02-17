import numpy as np
import SIZR

class PiecewiseSIZR(object):
    def __init__(self, var, time):
        self.var = var
        self.time = time

    def pw(self, t):
        time = self.time
        if 0<=t<=time[0]:
            return self.var[0]
        elif time[0]<=t<=time[1]:
            return self.var[1]
        elif time[1]<=t<=time[2]:
            return self.var[2]


if __name__ == "__main__":
    # Persistent variables
    time = [4, 28, 33]
    dt = 0.5
    ro = 1
    S0 = 60
    I0 = 0
    Z0 = 1
    R0 = 0
    T = 33
    sigma = PiecewiseSIZR([20, 2, 0], time)
    beta = PiecewiseSIZR([0.03, 0.0012, 0], time)
    deltas = PiecewiseSIZR([0, 0, 0.067], time)
    deltai = PiecewiseSIZR([0, 0.014, 0], time)
    alpha = PiecewiseSIZR([0, 0.0016, 0.006], time)
    war = SIZR.ProblemSIZR(sigma.pw, beta.pw, deltas.pw, deltai.pw, ro, alpha.pw, S0, I0, Z0, R0, T)
    solver = SIZR.SolverSIZR(war, dt)
    solver.solve()
    solver.show_war()
