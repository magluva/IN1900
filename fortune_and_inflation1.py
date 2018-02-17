import numpy as np

def A32_33(x0, c0, p, N, I=2):
    xn_val = np.empty(N+1)
    xn, cn = x0, c0
    n = 0
    while n <= N:
        tmp_x = xn + (p/100)*xn - cn
        tmp_c = cn +(I/100)*cn
        xn_val[n] = xn
        xn, cn = tmp_x, tmp_c
        n += 1
    return xn_val


def fortune_plot(y):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(y)
    ax.set_title("Fortune Plot")
    ax.set_xlabel("years")
    ax.set_ylabel("ammount")
    plt.legend(["liquidity"])
    return plt.show()

def main():
    p = 5
    q = 15
    N = 4
    x0 = 100
    c0 = ((p*q)/10**4)*x0
    fortune_plot(A32_33(x0, c0, p, N))

if __name__ == '__main__':
    main()
