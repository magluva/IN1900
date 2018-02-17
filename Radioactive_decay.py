import numpy as np
import ODESolver as solver


class Decay:
    "Contains physical properties for decay of C14"
    def __init__(self, a):
        self.a = a

    def __call__(self, u):
        return -self.a*u


class RK4(object):
    "Instantiate with object of Decay class"
    def __init__(self, obj):
        self.obj = obj

    def solve(self, u0, T, n):
        """
        Takes three args + Decay object.
        f = object.__call__
        u0 = initial value for problem
        T = number of years to advance through
        n = time step
        Returns time array as defined by T and n and u'
        """
        f = self.obj
        t = np.zeros(n+1)
        u = np.zeros(n+1)
        u[0] = u0
        t[0] = 0
        dt = T/n
        for k in range(n):
            t[k+1] = t[k]+dt
            k1 = dt*f(u[k])
            k2 = dt*f(u[k]+0.5*k1)
            k3 = dt*f(u[k]+0.5*k2)
            k4 = dt*f(u[k]+k3)
            u[k+1] = u[k]+(1/6)*(k1+2*k2+2*k3+k4)
        return u, t


def decay_plot(x0, y0, x1, y1):
    import matplotlib.pyplot as plt
    # Plot setup
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x0, y0, x1, y1)
    # Labeling
    ax.set_title("Radioactive Decay\nRunge Kutta 4")
    ax.set_xlabel("years")
    ax.set_ylabel("particles")
    ax.legend(["exact", "analytical"])
    # Display Tn values from exact and analytical solutions on figure
    ax.text(0.25, 0.1,"emax: {}\namax: {}".format(y0[-1], y1[-1]),\
            ha="center", va="center", transform=ax.transAxes)
    return plt.show()

def main():
    # Assigning values to needed variables
    a = np.log(2)/5600
    T = 20000
    n = int(10)
    u0 = 1
    # Init exact time and u' arrays
    et = np.linspace(0, T, n, True)
    eu = np.exp(-a*et)
    # Creating instances
    c14 = Decay(a)
    solver = RK4(c14)
    # Solving u' = -au
    au, at = solver.solve(u0, T, n)
    decay_plot(et, eu, at, au)

if __name__ == "__main__":
    main()

'''
You will find the emax for the last exact value and amax for the last
analytical value in the bottom left corner of the plot.
'''
