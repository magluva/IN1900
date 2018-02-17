# Python 3 (allways float division)

# All global variables are stored in ir_const.py
# and imported as constants due to scalability
# and it makes them easier to find/change.
# If you want me to keep all variables and "constants" in the main file,
# let me know via the feedback:)

# Fetching "constants" (need not assign to var)
from ir_const import A, P, N

def interest_rate(A, P, N):
    '''This function calculates interest rate and
    adds it to the start sum'''
    ans = A * (1 + (P / 100))**N
    return ans

# Recursive per year function inside a wrapper function.
# An iterative approach is better and more pythonic.
def wraper_func(A, P, N):
    y = (N -(N-1))

    def recu(A, P, y, stop=4):
        if(y == stop):
            return ""
        ans = A * (1 + (P / 100))**y
        print("Year {0}: {1:.3f}".format(y, ans))
        return recu(A, P, y+1)

    out = recu(A, P, y)
    return out



def main():

    # Function calls
    out = interest_rate(A, P, N)

    # Output
    # Can also call print(interest_rate.__doc__) if we want to.
    print("With a {0}% interest rate, {1} euros will become {2:.3f} in {3} years.".format(P, A, out, N))

    # Recursion test - per year:
    print("")
    print(wraper_func(A, P, N))

if __name__ == "__main__":
    main()

# Terminal Output:
'''
$ python interest_rate.py
With a 5% interest rate, 1000 euros will become 1157.625 in 3 years.

Year 1: 1050.000
Year 2: 1102.500
Year 3: 1157.625

'''
