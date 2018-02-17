import numpy as np

# Declaring f2c function()
def f2c(fahrenheit):
    return (fahrenheit - 32) * (5/9)

# Declaring f2c_approx function()
def f2c_approx(fahrenheit):
    return (fahrenheit - 30)/2

def my_plot(f):
    import matplotlib.pyplot as plt
    from matplotlib import style, patches
    # Creating a sensible legend
    red_patch = patches.Patch(color='red', label='approximation')
    blue_patch = patches.Patch(color='blue', label='exact')
    # Choosing theme
    style.use("seaborn-dark")
    # Creating figure object that will contain the axes objects.
    fig = plt.figure()
    # Axes object setup
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(f, f2c(f), "r", f, f2c_approx(f), "b")
    ax1.set_title("Farenheit to Celsius")
    ax1.legend(handles=[red_patch, blue_patch])
    return plt.show()

def main():
    # init f-array
    f = np.linspace(-20, 120, 1000)
    # plot function call
    my_plot(f)

if __name__ == '__main__':
    main()

# Terminal Output:
'''
None
The script just returns a plot.
'''
