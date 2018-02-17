import numpy as np
import SIR_class as parent

class ProblemSIRV(parent.ProblemSIR):
    def __init__(self, beta, nu, S0, I0, R0, T, p, V0):
        super(ProblemSIRV, self).__init__(beta, nu, S0, I0, R0, T)
        if isinstance(p, (float, int)):
            self.p = lambda t: p
        elif callable(p):
            self.p = p
        self.V0 = V0

    def __call__(self, u, t):
        S, I, R, V = u
        return np.array([-self.beta(t)*S*I-self.p(t)*S,\
                         self.beta(t)*S*I-self.nu(t)*I,\
                         self.nu(t)*I, self.p(t)*S])


class SolverSIRV(parent.SolverSIR):
    def __init__(self, problem, dt):
        self.problem = problem
        self.dt = dt

    def solve(self, method=parent.Rk4):
        n = int(self.problem.T/self.dt)
        t = np.linspace(0, self.problem.T, n, True)
        solver = method(self.problem)
        solver.set_init_cnd([self.problem.S0, self.problem.I0, self.problem.R0, self.problem.V0])
        u, self.t = solver.solve(t)
        # magic ziplike assignment
        self.S, self.I, self.R, self.V = u[:,0], u[:,1], u[:,2], u[:,3]

    def show_plot(self, betavalue=None, nuvalue=None, pvalue=None):
        import matplotlib.pyplot as plt
        import matplotlib.style as style
        # Setting up figure
        style.use("bmh")
        fig = plt.figure()
        # Setting up axes object
        ax = fig.add_subplot(1, 1, 1)
        if betavalue and nuvalue and pvalue is not None:
            ax.set_title("S.I.R.V Plot\nbeta: {}, v: {}, p {}".format(betavalue, nuvalue, pvalue))
        else:
            ax.set_title("S.I.R.V Plot")
        ax.set_xlabel("days")
        ax.set_ylabel("population")
        ax.plot(self.t, self.S)
        ax.plot(self.t, self.I)
        #print(self.I[idx], self.t[idx])
        ax.plot(self.t, self.R)
        ax.plot(self.t, self.V)
         # Max infected:
        for i, x in enumerate(self.I):
            if x == np.max(self.I):
                idx = i; break
        ax.plot(self.t, [self.I[idx] for i in self.t], color="green", linestyle=':')
        ax.legend(["Suseptable", "Infectious", "Recovered", "Vaccinated", "maximum infectious"])
        # Visualizing
        return plt.show()

if __name__ == "__main__":
    # Example variables
    S0 = 1500
    I0 = 1
    R0 = 0
    V0 = 0
    nu = 0.1
    # Making beta callable so we get desired change in value for t>12
    beta = lambda t: 0.0005 if t <= 12 else 0.0001 # beta = 0.0005
    p = 0.1
    T = 60
    dt = 0.5
    # Creating instance of ProblemSIR
    problem = ProblemSIRV(beta, nu, S0, I0, R0, T, p, V0)
    # Passing object of ProblemSir to instance of SolverSIR
    solver = SolverSIRV(problem, dt)
    # Solving
    solver.solve()
    # Plotting
    solver.show_plot(betavalue="0.0005 to 0,0001 where t=12", nuvalue=nu, pvalue=p)
