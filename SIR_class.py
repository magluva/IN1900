# -*- coding: utf-8 -*-
"""
@author: Magnus
"""
import sys
try:
    import numpy as np
except:
    print("module Numpy is missing: exiting ..."); sys.exit(1)


class ODE(object):
    def __init__(self, f):
        # Checking if f is callable
        if not callable(f):
            raise TypeError("No joy: f is not callable...")
        self.f = lambda u, t: np.asarray(f(u, t), float)

    def set_init_cnd(self, u0):
        # Checking if dealing with scalar or system of ODE for later
        if isinstance(u0, (float, int)):
            u0 = float(u0)
            self.size_u = 1
        else:
            u0 = np.asarray(u0)
            self.size_u = np.shape(u0)[0]
        self.u0 = u0

    def solve(self, tp):
        self.t = np.asarray(tp)
        n = self.t.size
        # Making 1D array or nD array for u depending on if scalar or system
        if self.size_u == 1:
            self.u = np.zeros(n)
        else:
            self.u = np.zeros((n, self.size_u))
        self.u[0] = self.u0
        # The loop
        for k in range(n-1):
            self.k = k
            self.u[k+1] = self.advance()
        return self.u[:k+2], self.t[:k+2]


class Rk4(ODE):
    # Advance method for Rk4(ODE). (ODE parent class cannot be used directly)
    def advance(self):
        u = self.u
        f = self.f
        k = self.k
        t = self.t
        dt = t[k+1] - t[k]
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + (1/2)*K1, t[k] + (1/2)*dt)
        K3 = dt*f(u[k] + (1/2)*K2, t[k] + (1/2)*dt)
        K4 = dt*f(u[k] + K3, t[k] + dt)
        _u = u[k] + (1/6)*(K1 + 2*K2 + 2*K3 + K4)
        return _u


class ProblemSIR(object):
    def __init__(self, beta, nu, S0, I0, R0, T):
        # Checking if beta and nu are numbers.
        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta
        if isinstance(nu, (float, int)):
            self.nu = lambda t: nu
        elif callable(nu):
            self.nu = nu
        # Initial conditions
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0
        self.T = T

    def __call__(self, u, t):
        S, I, R = u
        # The system of ODEs
        return np.array([-self.beta(t)*S*I,
                         self.beta(t)*S*I-self.nu(t)*I,
                         self.nu(t)*I])


class SolverSIR(object):
    def __init__(self, problem, dt):
        self.problem = problem
        self.dt = dt

    def solve(self, method=Rk4):
        # Setting up neccessary variables depending on problem object
        n = int(self.problem.T/self.dt)
        t = np.linspace(0, self.problem.T, n, True)
        solver = method(self.problem)
        solver.set_init_cnd([self.problem.S0, self.problem.I0, self.problem.R0])
        u, self.t = solver.solve(t)
        # magic ziplike assignment
        self.S, self.I, self.R = u[:,0], u[:,1], u[:,2]

    def show_plot(self, betavalue=None, nuvalue=None):
        import matplotlib.pyplot as plt
        import matplotlib.style as style
        # Setting up figure
        style.use("bmh")
        fig = plt.figure()
        # Setting up axes object
        ax = fig.add_subplot(1, 1, 1)
        if betavalue and nuvalue is not None:
            ax.set_title("S.I.R Plot\nbeta: {}, v: {}".format(betavalue, nuvalue))
        else:
            ax.set_title("S.I.R Plot")
        ax.set_xlabel("days")
        ax.set_ylabel("population")
        ax.plot(self.t, self.S)
        ax.plot(self.t, self.I)
        #print(self.I[idx], self.t[idx])
        ax.plot(self.t, self.R)
         # Max infected:
        for i, x in enumerate(self.I):
            if x == np.max(self.I):
                idx = i; break
        ax.plot(self.t, [self.I[idx] for i in self.t], color="green", linestyle=':')
        ax.legend(["Suseptable", "Infectious", "Recovered", "maximum infectious"])
        # Visualizing
        return plt.show()


if __name__ == "__main__":
    # Example variables
    S0 = 1500
    I0 = 1
    R0 = 0
    v = 0.1
    # Making beta callable so we get desired change in value for t>12
    beta = lambda t: 0.0005 if t <= 12 else 0.0001 # beta = 0.0005
    T = 60
    dt = 0.5
    # Creating instance of ProblemSIR
    problem = ProblemSIR(beta, v, S0, I0, R0, T)
    # Passing object of ProblemSir to instance of SolverSIR
    solver = SolverSIR(problem, dt)
    # Solving
    solver.solve()
    # Plotting
    solver.show_plot(betavalue="0.0005 to 0,0001 where t=12", nuvalue=v)






"""
Beta = 0.005:
Predicts a max infectious value of 897.177648467 people after
14.62184874 days

Beta = 0.005 if t<=12 else 0.001:
Predicts a max infectious value of 744.884042958 people after
12.1008403361 days
"""
