
def main():

    # Defining variables
    g = 9.81
    v0 = 5
    n = 10
    t_space = 2 * v0 / g / n

    # List comprehension
    t = [i*t_space for i in range(0, n+1)]
    y = [v0 * t[i] -(1/2) * g * t[i]**2 for i in range(0, len(t))]

    ty1 = [t, y]
    ty2 = [e for e in zip(t, y)]

    # Output ty1
    print("\n{0:10}{1}".format("t", "y(t)"))
    for k, m in zip(ty1[0], ty1[1]):
        print("{0:.3f}{1:10.3f}".format(k, m))

    # Output ty1
    print("\n{0:10}{1}".format("t", "y(t)"))
    for k, m in ty2:
        print("{0:.3f}{1:10.3f}".format(k, m))



if __name__ == '__main__':
    main()

# Terminal Output:
'''
$ python ball_table3.py

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

'''
