import numpy as np
import SIRV

def optimize(beta, nu, S0, I0, R0, T, p, V0, dt, vp):
    imax = np.zeros(vp+1)
    period = np.arange(vp+1)
    for i in range(vp+1):
        p = lambda t: 0.1 if 6<=t<=6+i else 0
        problem = SIRV.ProblemSIRV(beta, nu, S0, I0, R0, T, p, V0)
        solver = SIRV.SolverSIRV(problem, dt)
        solver.solve()
        imax[i] = np.max(solver.I)
    show_plot(period, imax)

def get_best(x, y):
    # We know y -> 0 so we fetch the max value first then break on the first min index
    for idx, var in enumerate(y):
        if var == np.max(y):
            maxidx = idx
        elif var == np.min(y):
            minidx = idx
            break
    return x[minidx], x[maxidx], y[minidx], y[maxidx]

def show_plot(x, y):
    import matplotlib.pyplot as plt
    import matplotlib.style as style
    # Setting up figure
    style.use("bmh")
    fig = plt.figure()
    # Setting up axes object
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y)
    ax.set_title("Vaccination period")
    ax.set_xlabel("days")
    ax.set_ylabel("people")
    ax.legend(["max infected"])
    xmax, xmin, ymin, ymax = get_best(x, y)
    ax.text(0.5, 0.5,
            "-------------------------------------\n"+\
            "Max Infected: {0:>10.3f}\n".format(ymax)+\
            "Max Infected: {0:>10.3f}\n".format(ymin)+\
            "Viable period: {0:>10.0f}\n".format(xmax-xmin)+\
            "-------------------------------------\n",
            transform=ax.transAxes)
    return plt.show()

if __name__ == "__main__":
    # Example variables
    S0 = 1500
    I0 = 1
    R0 = 0
    V0 = 0
    nu = 0.1
    # Making beta callable so we get desired change in value for t>12
    beta = 0.0005 # beta = 0.0005
    T = 60
    dt = 0.5
    vp = 31

    optimize(beta, nu, S0, I0, R0, T, vp, V0, dt, vp)
