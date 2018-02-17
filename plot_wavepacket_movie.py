import numpy as np
import os
import glob

# Wavepacket function
def f(x, t=0):
    return np.exp(-(x-3*t)**2) * np.sin(3*np.pi*(x-t))

# Remove generated png files function
def rm_png():
    for filename in glob.glob('tmp*.png'):
        os.remove(filename)
    return

# Animation function
def animation(t_min=-1, t_max=1, x_min=-6, x_max=6, f_no=60):
    from matplotlib import pyplot as plt
    import matplotlib.style as style
    style.use("seaborn-poster")
    x_val = np.linspace(x_min, x_max, 1000, True)
    init = np.empty(x_val.shape[0])
    # Animation init
    lines = plt.plot(x_val, init)
    plt.axis([x_min, x_max, t_min, t_max])
    # Init t_val array for number of frames total
    t_val = np.linspace(t_min, t_max, f_no+1)
    counter = 0
    # Generate pngs
    for t in t_val:
        y = f(x_val, t)
        # Evolving t_data in variable lines
        lines[0].set_ydata(y)
        plt.legend(["Wavepacket"])
        plt.xlabel("x")
        plt.ylabel("Amplitude")
        plt.draw()
        plt.pause(0.01)
        plt.savefig("tmp_{0:04d}.png".format(counter))
        counter += 1
    return

def main():
    # Remove old pngs if present.
    rm_png()
    # Calling animation function
    animation()
    # Using unix command to convert to gif
    os.system("convert -delay 10 -loop 0 tmp*.png awesome.gif")
    # Removes tmp*.png if present.
    rm_png()

if __name__ == '__main__':
    main()
