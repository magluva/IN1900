import numpy as np

def y(t):
    A = 0.3 # m
    m = 9 # kg
    k = 4 # kg/s^2
    l = 0.15 # s^-1
    return A * np.exp(l*t) * np.cos((np.sqrt(k/m) * t))

def my_plot(xa, ya, xb, yb):
    import matplotlib.pyplot as plt
    from matplotlib import style, patches
    # Creating a sensible legend
    green_patch = patches.Patch(color='green', label='a-values')
    blue_patch = patches.Patch(color='blue', label='b-values')
    # Choosing theme
    style.use("seaborn-dark")
    # Creating figure object that will contain the axes objects.
    fig = plt.figure()
    # Shared plot setup
    ax1 = fig.add_subplot(3, 1, 1)
    ax1.plot(xa, ya, "g")
    ax1.plot(xb, yb, "b")
    ax1.set_title("Oscilating Spring")
    ax1.legend(handles=[green_patch, blue_patch])
    # a-values only setup
    ax2 = fig.add_subplot(3, 1, 2, sharex=ax1, sharey=ax1)
    ax2.plot(xa, ya, "g")
    ax2.set_ylabel("Position")
    ax2.legend(handles=[green_patch])
    # b-values only setup
    ax3 = fig.add_subplot(3, 1, 3, sharex=ax1, sharey=ax1)
    ax3.plot(xb, yb, "b")
    ax3.legend(handles=[blue_patch])
    ax3.set_xlabel("Time")
    return plt.show()

def main():
    n = 101
    dt = 25 / (n-1)
    
    # a)
    t_array = np.zeros(n)
    y_array = np.zeros(n)
    for i in range(n):
        t_array[i] = i*dt
        y_array[i] = y(i*dt)
    xa = t_array.copy()
    ya  = y_array.copy()

    # b)
    t_array = np.linspace(0, 25, n)
    # This code will work without np.vectorize, and would
    # return <class numpy.ndarray> bacause we passed y(x) an object of that type.
    # To be sure it works if we pass in a list, I vectorized it.
    y_vec = np.vectorize(y)
    y_array = y_vec(t_array)

    # c)
    my_plot(xa, ya, t_array, y_array)
    # All use of pyplot is contained in my_plot()'s local scope.
    # This is so I don't waste resources if i dont want to show plot.

if __name__ == '__main__':
    main()

# Terminal Output:
'''
This script produces a plot.
run "python Oscilating_spring.py" and
magic will happen!

NB: In the first subplot the lines are on top of eachother.
You will not be able to see both, only that the "line" is a bit thicker.
'''
