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
        if self.size_u is 1:
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

class ProblemSIZR(object):
    def __init__(self, sigma, beta, deltas, deltai, ro, alpha, S0, I0, Z0, R0, T):
        if isinstance(sigma, (float, int)):
            self.sigma = lambda t: sigma
        elif callable(sigma):
            self.sigma = sigma
        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta
        if isinstance(deltas, (float, int)):
            self.deltas = lambda t: deltas
        elif callable(deltas):
            self.deltas = deltas
        if isinstance(deltai, (float, int)):
            self.deltai = lambda t: deltai
        elif callable(deltai):
            self.deltai = deltai
        if isinstance(ro, (float, int)):
            self.ro = lambda t: ro
        elif callable(ro):
            self.ro = ro
        if isinstance(alpha, (float, int)):
            self.alpha = lambda t: alpha
        elif callable(alpha):
            self.alpha = alpha
        self.S0 = S0
        self.I0 = I0
        self.Z0 = Z0
        self.R0 = R0
        self.T = T

    def __call__(self, u, t):
        S, I, Z, R = u
        return np.array([
                         self.sigma(t)-self.beta(t)*S*Z-self.deltas(t)*S,
                         self.beta(t)*S*Z-self.ro(t)*I-self.deltai(t)*I,
                         self.ro(t)*I-self.alpha(t)*S*Z,
                         self.deltas(t)*S+self.deltai(t)*I+self.alpha(t)*S*Z])


class SolverSIZR(object):
    def __init__(self, war, dt):
        self.war = war
        self.dt = dt

    def solve(self, method=Rk4):
        n = self.war.T/self.dt
        t = np.linspace(0, self.war.T, n, True)
        solver = method(self.war)
        solver.set_init_cnd([self.war.S0, self.war.I0, self.war.Z0, self.war.R0])
        u, self.t = solver.solve(t)
        self.S, self.I, self.Z, self.R = u[:,0], u[:,1], u[:,2], u[:,3]

    def show_war(self):
        import matplotlib.pyplot as plt
        import matplotlib.style as style
        # Setting up figure
        style.use("bmh")
        fig = plt.figure()
        # Setting up axes object
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(self.t, self.S)
        ax.plot(self.t, self.I)
        ax.plot(self.t, self.Z)
        ax.plot(self.t, self.R)
        ax.set_title("Zombies vs. Humans")
        ax.set_xlabel("hours")
        ax.set_ylabel("soldiers")
        ax.legend(["Suseptable Humans", "Infectious Humans", "Zombies", "Dead"])
        return plt.show()

if __name__ == "__main__":
    S0 = 10
    I0 = 0
    Z0 = 100
    R0 = 0
    sigma = 2
    beta = 0.0012
    deltas = 0
    deltai = 0.014
    ro = 1
    alpha = 0.0016
    T = 24
    dt = 0.5

    war = ProblemSIZR(sigma, beta, deltas, deltai, ro, alpha, S0, I0, Z0, R0, T)
    solver = SolverSIZR(war, dt)
    solver.solve()
    solver.show_war()
