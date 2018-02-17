import numpy as np

# Approximate function
def s(t, n, T):
    temp = 0
    for i in range(1, n+1):
        temp += (1/(2*i-1)*np.sin((2*(2*i-1)*np.pi*t)/T))
    temp *= 4/np.pi
    return temp

# Exact function
def f(t, T):
    if t > 0 and t < T/2:
        return 1
    elif t == T/2:
        return 0
    elif t > T/2 and t < T:
        return -1

# Vectorizing f(t, T) in stead of changing to .all() for
# evaluating thruth values for list
f_vec = np.vectorize(f)

def my_plot(t, n, T):
    import matplotlib.pyplot as plt
    import matplotlib.style as style
    style.use("seaborn-poster")
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Sinesum Plot")
    ax.set_xlabel("t-values")
    ax.set_ylabel("sinesum-values")
    # Plotting the different n-values with for loop
    for i in n:
        ax.plot(t, s(t, i, T))
    ax.plot(t, f_vec(t, T))
    plt.legend(["n=1", "n=3", "n=20", "n=200", "f(t)"])
    return plt.show()

def main():

    # init n-list
    # To skip vectorizing step you could do np.array([1, 3, 20, 200]),
    # which is probably better to be honest.
    n = [1, 3, 20, 200]
    T = 2*np.pi
    # init t-array
    t = np.linspace(0.01, T-0.01, 1000)
    # Calling plot function
    my_plot(t, n ,T)

if __name__ == '__main__':
    main()

# Terminal Output:
'''
None. Produces a plot.
The accuracy of the approximation increases with n.
'''
