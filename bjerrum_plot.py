import numpy as np

# punction for calculating the y-values
def eq(haq, k1=5.01e-7, k2=4.79e-11):
    co2aq = (haq**2)/((haq**2)+(k1*haq)+(k1*k2))
    hco3aq = (k1*(haq))/((haq**2)+(k1*haq)+(k1*k2))
    co3aq = (k1*k2)/((haq**2)+(k1*haq)+(k1*k2))
    return co2aq, hco3aq, co3aq

# plot function
def eq_plot(x, y0, y1, y2):
    import matplotlib.pyplot as plt
    import matplotlib.style as style
    style.use("Solarize_Light2")
    # fig setup
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y0, x, y1, x, y2)
    # labeling
    ax.set_title("Bjerrum Plot")
    ax.set_xlabel("pH")
    ax.set_ylabel("concentration")
    # find intersections CO2 and HCO3
    idx0 = np.argwhere(np.diff(np.sign(y0 - y1)) != 0).reshape(-1) + 0
    i0 = [x[idx0], y0[idx0]]
    ax.plot(i0[0], i0[1], "ro")
    print("CO2(aq) and HCO3⁻(aq) intersect at coordinates (x, y):\n{}".format(i0))
    # find intersections HCO3⁻ and CO3²⁻
    idx1 = np.argwhere(np.diff(np.sign(y1 - y2)) != 0).reshape(-1) + 0
    i1 = [x[idx1], y1[idx1]]
    ax.plot(i1[0], i1[1], "ro")
    print("CO2(aq) and HCO3⁻(aq) intersect at coordinates (x, y):\n{}".format(i1))
    plt.legend(["Carbon cioxide", "Bicarbonate", "Carbonate", "Intersections"])
    return plt.show()

def main():
    # init pH array
    pH = np.linspace(4, 12, 1000, True)
    # init H+aq array
    haq = 10**(-pH)
    # unpacking eq() values
    y0, y1, y2 = eq(haq)
    # calling plot function
    eq_plot(pH, y0, y1, y2)

if __name__ == '__main__':
    main()

# Terminal Output:
'''
The program returns a plot and b) coordinates.

$ python bjerrum_plot.py
CO2(aq) and HCO3⁻(aq) intersect at coordinates (x, y):
[array([ 6.2982983]), array([ 0.50104919])]
CO2(aq) and HCO3⁻(aq) intersect at coordinates (x, y):
[array([ 10.31831832]), array([ 0.50075087])]
'''
