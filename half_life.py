from math import e, log

# Fixed K-11 func() with provided values
def N_k11(t):
    N0 = 4.5
    r = 1760
    ans = N0 * e**(-t/r)
    return ans

# time_const as wrapper for new K-11 func()
def time_const(t):
    t_half = 1220
    r = t_half / log(2)
    def N_K11(r ,t):
        N0 = 4.5
        ans = N0 * e**(-t/r)
        return ans
    ans = N_K11(r, t)
    return r, ans

# Not so accurate test func(). Provided values held no decimal points
def my_test(a, b):
    a1 = 1760
    a2 = a
    b1 = b[0]
    b2 = b[1]
    tol = 0.1
    success = abs(a1 - b1) < tol and abs(a2 - b2) < tol
    if success:
        print("Inaccurate Test Passed...")
    else:
        print("Inaccurate Test Failed. wow...")


def main():

    # declaring variables
    t = 10 * 60
    tmin = 0
    tmax = 10**6

    # Function calls for Oppg a)
    a = N_k11(t)
    a_test1 = N_k11(tmin)
    a_test2 = N_k11(tmax)
    # Output Oppg a)
    print("\nResults from a)")
    print("K-11 after 10 minutes: {} kg\nTest small: {} kg\nTest large: {} kg\n".format(a, a_test1, a_test2))

    # Function calls Oppg b)
    b = time_const(t)
    # Output Oppg b)
    print("Results from b):\nTime constant: {}\nAmmount: {}\n".format(b[0], b[1]))

    # Function call test func()
    my_test(a, b)

if __name__ == '__main__':
    main()

# Terminal Output:
'''
$ python half_life.py

Results from a)
K-11 after 10 minutes: 3.20005598788659 kg
Test small: 4.5 kg
Test large: 7.852069946502651e-247 kg

Results from b):
Time constant: 1760.0879498845354
Ammount: 3.2001105009718582

Inaccurate Test Passed...

'''
