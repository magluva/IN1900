# coding: utf8
# Jeg gjør oppgavene i løp 2 ved siden av:)

# Declaring f2c function()
def f2c(fahrenheit):
    return (fahrenheit - 32) * (5/9)

# Declaring f2c_approx function()
def f2c_approx(fahrenheit):
    return (fahrenheit - 30)/2


def main():

    # Declaring and initializing variables.
    f = 0
    n = 100

    # Output:
    # While loop prints formatted table; incremented by 10; added diff.
    print("\n  {0:10}{1:10}{2:10}{3}\n".format("F", "C", "Ĉ", "|C|-|Ĉ|"))
    while f <= n:
        c = f2c(f)
        c_approx = f2c_approx(f)
        diff = abs(c -c_approx)
        print("{0:3d} {1:10.3f} {2:10.3f} {3:10.2f}".format(f, c, c_approx, diff))
        f +=10

if __name__ == '__main__':
    main()

# Terminal Output:
'''
$ python f2c_approx_table.py

  F         C         Ĉ         |C|-|Ĉ|

  0    -17.778    -15.000       2.78
 10    -12.222    -10.000       2.22
 20     -6.667     -5.000       1.67
 30     -1.111      0.000       1.11
 40      4.444      5.000       0.56
 50     10.000     10.000       0.00
 60     15.556     15.000       0.56
 70     21.111     20.000       1.11
 80     26.667     25.000       1.67
 90     32.222     30.000       2.22
100     37.778     35.000       2.78
'''
