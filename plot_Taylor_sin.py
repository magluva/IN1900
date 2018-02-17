import numpy as np
from math import factorial

# Taylor function
def S(x, n):
    s = 0
    for j in range(0, n+1):
        # += produces problems with large value np.arrays so s = s+x
        s = s + (((-1)**j)*((x**(2*j+1))/factorial((2*j+1))))
    return s

def taylor_plot(x, n):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # plotting sin(x)
    ax.plot(x, np.sin(x))
    # plotting for each n
    for i in n:
        ax.plot(x, S(x, i))
    ax.set_title("Taylor sin")
    ax.set_xlabel("x")
    ax.set_ylabel("sin(x)")
    plt.legend(["accurate", "n=1", "n=2", "n=3", "n=6", "n=12"])
    return plt.show()

def main():
    # init x array
    x = np.linspace(0, 4*np.pi, 100)
    n = [1, 2, 3, 6, 12]
    # calling plot function
    taylor_plot(x, n)

if __name__ == '__main__':
    main()
