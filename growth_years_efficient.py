x0 = 100
p = 5
N = 4

xn = x0
n = 0
with open("growth.dat", "a") as f:
    f.write("{0} {1:^20}\n".format("n", "xn"))
    while n <= N:
        tmp = xn + (p/100.)*xn
        f.write("x{0:^1} {1:^20.6f}\n".format(n, xn))
        xn = tmp
        n += 1
