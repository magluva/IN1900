import numpy as np

# Reading from file: return nested list
def read_file(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        data  = [i.split() for i in lines]
    return data

# Unpacking and assigning elements to arrays: return 1x2 touple of arrays
def nest_to_arr(data):
    l = np.shape(data)[0]
    x_arr = np.empty(l-1)
    y_arr = np.empty(l-1)
    for ii, i in enumerate(data[1::]):
        x_arr[ii] = float(i[0])
        y_arr[ii] = float(i[1])
    return x_arr, y_arr

# Forward x-velocity: return array
def vxy(x, tk, s, n):
    v = np.empty(n)
    c = 0
    for i, k in zip(x, tk):
        v[c] = (i*(k+1)-i*k)/s
        c += 1
    return v

# Plot function: return plot
def v_plot(*args):
    import matplotlib.pyplot as plt
    import matplotlib.style as style
    style.use("seaborn-poster")
    # Unpacking args: using k-values as time
    # k has same first dimension and contains suitable numeric values
    n, x, y, vx, vy, time = args
    fig = plt.figure()
    # x vs y plot setup
    ax1 = fig.add_subplot(3, 1, 1)
    ax1.plot(x, y, "r", linestyle="-.")
    ax1.legend(["xy"], loc=1)
    ax1.set_title("Position to Velocity")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.grid(True)
    # time vs x-velocity plot setup
    ax2 = fig.add_subplot(3, 1, 2)
    ax2.plot(time, vx, "g")
    ax2.legend(["vx"], loc=4)
    ax2.set_xlabel("time")
    ax2.set_ylabel("x-velocity")
    # time vs y-velocity plot setup
    ax3 = fig.add_subplot(3, 1, 3, sharex=ax2)
    ax3.plot(time, vy, "b")
    ax3.legend(["vy"], loc=1)
    ax3.set_xlabel("time")
    ax3.set_ylabel("y-velocity")
    return plt.show()

def main():
    # Storing data as nested list in data variable.
    # If dealing with a large file read_file() should yield a generator
    data = read_file("pos.dat")
    # Assigning s-value directky
    s = float(data[0][0])
    # Creating position arrays
    x, y = nest_to_arr(data)
    # Init n, k and tk arrays
    n = np.shape(data)[0]-1
    k = np.linspace(0, (n - 1), int(n), True)
    tk = s*k
    # Creating velocity arrays
    vx = vxy(x, tk, s, n)
    vy = vxy(y, tk, s, n)
    # Calling plot function to display fig
    v_plot(n, x, y, vx, vy, k)


if __name__ == '__main__':
    main()
