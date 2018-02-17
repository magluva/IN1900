import numpy as np

def f(u, t):
    return u

def RungeKutta2(f, U0, T, n):
    t = np.zeros(n+1)
    u = np.zeros(n+1)
    u[0] = U0
    t[0] = 0
    dt = T/n
    for k in range(n):
        t[k+1] = t[k] + dt
        k1 = dt*f(u[k], t[k])
        k2 = dt*f(u[k]+0.5*k1, t[k]+0.5*dt)
        u[k+1] = u[k]+k2
    return u, t

def rk2_plot(x0, y0, x1, y1):
    import matplotlib.pyplot as plt
    import matplotlib.style as style
    style.use("seaborn-dark")
    fig = plt.figure()
    ax1 = fig.add_subplot(3, 1, 1)
    ax1.plot(x0[0], y0[0], x1[0], y1[0])
    ax1.set_title("Runge Kutta 2: T=25")
    ax1.legend(["exact", "analytical"])
    ax2 = fig.add_subplot(3, 1, 2)
    ax2.plot(x0[1], y0[1], x1[1], y1[1])
    ax2.set_title("Runge Kutta 2: T=15")
    ax2.set_ylabel("exp(t)")
    ax2.legend(["exact", "analytical"])
    ax3 = fig.add_subplot(3, 1, 3)
    ax3.plot(x0[2], y0[2], x1[2], y1[2])
    ax3.set_title("Runge Kutta 2: T=5")
    ax3.set_xlabel("t")
    ax3.legend(["exact", "analytical"])
    return plt.show()

def main():
    # Assinging values
    T = np.array([25, 15, 4])
    U0 = 1
    n = 25
    # Init arrays
    t_e = [np.linspace(0, i, 1000, True) for i in T]
    u_e = [np.exp(i) for i in t_e]
    rk = [RungeKutta2(f, U0, i, n) for i in T]
    u_a = [rk[0][0], rk[1][0], rk[2][0]]
    t_a = [rk[0][1], rk[1][1], rk[2][1]]
    # Calling plot function
    rk2_plot(t_e, u_e, t_a, u_a)

if __name__ == "__main__":
    main()

'''
I would suggest viewing the plots in fullscreen.
We can see that when T is large in subplot 1 and gets
smaller and smaller until subplot 3, our analytical
solution gets more accurate.
'''
