import numpy as np

# Function reads file and assigns to array: return 1*3 touple of ndarrays
def process_file(filename):
    data = []
    with open(filename, "r") as f:
        for lines in f:
            # appends only lines containing epsilon values to data-list
            if "epsilon" in lines:
                data.append(lines.strip())
    # Splits data elements in to nested list
    _ls = [i.split() for i in data]
    # Explicit assignments of nested elements to new lists
    eps = [float(_[1].strip(",")) for _ in _ls]
    err = [float(_[4].strip(",")) for _ in _ls]
    n = [float(_[5][2::]) for _ in _ls]
    # Converts to ndarray
    return np.array(eps), np.array(err), np.array(n)

# Plot function: return plot
def eps_err_plot(x, y0, y1):
    import matplotlib.pyplot as plt
    import matplotlib.style as style
    style.use("seaborn-poster")
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.semilogy(x, y0, x, y1)
    ax.set_title("Epsilon Error Plot")
    ax.set_xlabel("n")
    ax.set_ylabel("log")
    ax.legend(["epsilon", "error"], loc=1)
    return plt.show()


def main():
    # Calling function, unpacking touple and assigning to variables
    epsilon, error, n = process_file("lnsum.dat")
    # Plot call
    eps_err_plot(n, epsilon, error)

if __name__ == "__main__":
    main()
