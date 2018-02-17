import numpy as np
import SIZR

class Alpha(object):
    def __init__(self, time, alpha, beta, sigma):
        self.time = time
        self.alpha = alpha
        self.beta = beta
        self.sigma = sigma

    def omega(self, t):
        alpha = self.alpha*self.beta
        a = 50*alpha
        n = len(self.time)
        arr = np.zeros(n)
        for i in range(n):
            arr[i] = np.exp(-(1/2)*((t-self.time[i])/self.sigma)**2)
        return alpha+(a*np.sum(arr))



if __name__ == "__main__":
        # source /opt/anaconda/bin/activate root
        S0 = 50
        I0 = 0
        Z0 = 3
        R0 = 0
        sigma = 0
        beta = 0.03
        deltas = 0
        deltai = 0.0
        ro = 1
        T = 20
        dt = 0.5
        alpha = Alpha([5, 10, 18], 0.2, beta, 0.5)

        war = SIZR.ProblemSIZR(sigma, beta, deltas, deltai, ro, alpha.omega, S0, I0, Z0, R0, T)
        solver = SIZR.SolverSIZR(war, dt)
        solver.solve()
        solver.show_war()
