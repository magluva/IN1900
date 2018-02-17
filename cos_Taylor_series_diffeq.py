import numpy as np
########################################
##   a)                               ##
##   a{j} = -a{j-1}*(x²/(2*j)*2*j)    ##
##   s{j} = s{j-1} + a{j-1}           ##
##                                    ##
########################################

# Taylor function using numpy arrays: return 1*2 touple of s{n+1}, |a{n+1}|
def cos_Taylor(x, n):
    a = np.empty(n+2)
    s = np.empty(n+2)
    a[0] = 1; s[0] = 0
    for j in range(1, n+2):
        a[j] = -a[j-1]*(x**2/((2*j)*2*j))
        s[j] = s[j-1]+a[j-1]
    return s[n+1], abs(a[n+1])

# Plot function: return plot
def cos_Taylor_plot():
    import matplotlib.pyplot as plt
    import matplotlib.style as style
    style.use("bmh")
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    # Found no other way but to vectorize here. It is not optimal,
    # but was done to bypass ValueError and bug in cos_Taylor() array initialization.
    # The function could be reimplemented without arrays to circumvent this
    vcT = np.vectorize(cos_Taylor)
    x_val = np.linspace(0,3*np.pi, 1000, True)
    n_val = np.linspace(1, 1000, 1000, True, dtype=np.int)
    ax1.plot(x_val, np.cos(x_val), x_val, vcT(x_val, n_val)[0])
    ax1.set_title("Cos-Taylor Plot")
    ax1.set_xlabel("x")
    ax1.set_ylabel("cos(x)")
    ax1.legend(["exact", "approx"])
    return plt.show()

# Straightforward test function with values from Glorious Casio
def cos_Taylor_test():
    x = np.pi; n = 2
    expected = 0.05461594713394846
    computed = cos_Taylor(x, n)[0]
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = "expected {} != {} (computed)".format(expected, computed)
    assert success, msg

def main():
    # Function calls
    cos_Taylor_plot()
    cos_Taylor_test()

    # This program was only intended to solve this exercise with set
    # values. Generally this is bad practice.
if __name__ == '__main__':
    main()

# Output:
'''
Plot:
We clearly see that while x is small and y is large, we are closest to
the exact values. As the plot unfolds, accuracy gets worse.
'''
