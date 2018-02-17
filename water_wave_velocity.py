import numpy as np

def c(l, h):
    g = 9.81 # m/s^2
    s = 7.9E-2 # N/m
    p = 1000 # kg/m^3
    return np.sqrt(((g*l)/(2*np.pi)) * \
           (1+s*((4*np.pi**2)/(p*g*l**2))) * \
           np.tanh((2*np.pi*h)/(l)))

def my_plot(l1, l2, h=50):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    # Subplot 1 setup
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.set_xlabel("m")
    ax1.set_ylabel("m/s")
    ax1.plot(l1, c(l1, h))
    # Subplot 2 setup
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.set_xlabel("m")
    ax2.set_ylabel("m/s")
    ax2.plot(l2, c(l2, h))
    return plt.show()

def main():

    # init l_small array
    l_small = np.linspace(0.001, 0.1, 1000)
    # init l_large array
    l_larger = np.linspace(1, 2000, 10000)
    # Calling plot function
    my_plot(l_small, l_larger)

if __name__ == '__main__':
    main()
