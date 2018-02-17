import numpy as np

def f(x, t=0):
    return np.exp(-(x-3*t)**2) * np.sin(3*np.pi*(x-t))

def my_plot(x):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_title("Wavepacket")
    ax1.set_xlabel("x")
    ax1.set_ylabel("Amplitude")
    ax1.plot(x, f(x))
    return plt.show()


def main():
    # init x-array
    x = np.linspace(-4, 4, 1000)
    # Calling plot function
    my_plot(x)


if __name__ == '__main__':
    main()
