def test_max(t, y, v0, g):
    success = 2

    tmax =  2 * v0 / g
    ymax = v0 * tmax -(1/2) * g * tmax**2

    if t[-1] == tmax:
        success -= 1
    else: print("List: t, MaxValueError")
    if y[-1] == ymax:
        success -= 1
    else: print("List: y, MaxValueError")

    print("\nRan test.\n{} errors found.".format(success))


def main():

    # Defining variables
    g = 9.81
    v0 = 5
    n = 10
    t_space = 2 * v0 / g / n

    # List comprehension
    t = [i*t_space for i in range(0, n+1)]
    y = [v0 * t[i] -(1/2) * g * t[i]**2 for i in range(0, len(t))]

    # Foor-loop solution
    print("\n{0:10}{1}".format("t", "y(t)"))
    for k, m in zip(t, y):
        print("{0:.3f}{1:10.3f}".format(k, m))

    # While loop solution
    inc = 0
    print("\n{0:10}{1}".format("t", "y(t)"))
    while inc < n+1:
        print("{0:.3f}{1:10.3f}".format(t[inc], y[inc]))
        inc += 1

    test_max(t, y, v0, g)

if __name__ == '__main__':
    main()

# Console Output:
'''
$ python ball_table2.py

t         y(t)
0.000     0.000
0.102     0.459
0.204     0.815
0.306     1.070
0.408     1.223
0.510     1.274
0.612     1.223
0.714     1.070
0.815     0.815
0.917     0.459
1.019     0.000

t         y(t)
0.000     0.000
0.102     0.459
0.204     0.815
0.306     1.070
0.408     1.223
0.510     1.274
0.612     1.223
0.714     1.070
0.815     0.815
0.917     0.459
1.019     0.000

Ran test.
0 errors found.
'''
