from numpy import sqrt, exp, pi

# Defining gauss function()
def gaussian2(x, m=0, s=1):
    for i in x:
        ans =(1/(sqrt(2 * pi) * s)) * exp((-1/2) * ((i - m)/s)**2)
        print("{0:5.2f} {1:10f}".format(i, ans))
    return

def main():
    # Declaring and initializing variable(s)
    m = 0; s = 1
    lim = [m - (5 * s), m + (5 * s)]
    n = 10
    # List comprehention of x values
    x = [lim[0] + i * ((lim[1] - lim[0]) / (n-1)) for i in range(n)]

    # Output
    print("\n {0:6s}{1:10s}".format("x", "f(x)"))
    print("-------------------------------------")
    # Function call. gaussian2() contains call to print.
    gaussian2(x)

    # This particular way of presenting x and f(x) with pre-initialized values would be more
    # useful (in my opinion) if the function took m, s, n as parameters.
    # That way you could get a dynamic table based on user min/max values f.ex.
    # if loaded as a module.
def gaussian2_dynamic(m=0, s=1, n=10):
    lim = [m - (5 * s), m + (5 * s)]
    x = [lim[0] + i * ((lim[1] - lim[0]) / (n-1)) for i in range(n)]
    for i in x:
        ans =(1/(sqrt(2 * pi) * s)) * exp((-1/2) * ((i - m)/s)**2)
        print("{0:5.2f} {1:10f}".format(i, ans))

if __name__ == '__main__':
    main()

# Terminal Output:
'''
$ python gaussian2.py

 x     f(x)
-------------------------------------
-5   0.000001
-4   0.000134
-3   0.004432
-2   0.053991
-1   0.241971
 0   0.398942
 1   0.241971
 2   0.053991
 3   0.004432
 4   0.000134
 5   0.000001

'''
