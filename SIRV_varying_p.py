import SIRV

if __name__ == "__main__":
    # Example variables
    S0 = 1500
    I0 = 1
    R0 = 0
    V0 = 0
    nu = 0.1
    # Making beta callable so we get desired change in value for t>12
    beta = lambda t: 0.0005 if t <= 12 else 0.0001 # beta = 0.0005
    p = lambda t: 0.1 if 6<=t<=15 else 0
    T = 60
    dt = 0.5
    # Creating instance of ProblemSIR
    problem = SIRV.ProblemSIRV(beta, nu, S0, I0, R0, T, p, V0)
    # Passing object of ProblemSir to instance of SolverSIR
    solver = SIRV.SolverSIRV(problem, dt)
    # Solving
    solver.solve()
    # Plotting
    solver.show_plot()
