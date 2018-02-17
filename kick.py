
# All global variables are stored in ir_const.py
# and imported as constants due to scalability
# and it makes them easier to find/change.
# If you want me to keep all variables and "constants" in the main file,
# let me know via the feedback:)

# Fetching "constants" (need not assign to var)
from kick_const import Cd, Q, A, Vh, Vs, M, G


def drag(Cd, Q, A, V):
    '''Calculates drag force.
    Takes four args, returns long.'''
    ans = (1/2) * Cd * Q * A * V**2
    return ans

def grav(M, G):
    '''Calculates gravity force.
    Takes two args, returns long.'''
    ans = M * G
    return ans

def ratio(x, y):
    '''Calculates ratio.
    Takes two args, returns long.'''
    ans = x / y
    return ans

def main():

    # Function calls
    fd_hard_kick = drag(Cd, Q, A, Vh)
    fd_soft_kick = drag(Cd, Q, A, Vs)
    fg = grav(M, G)
    r_hard = ratio(fd_hard_kick, fg)
    r_soft = ratio(fd_soft_kick, fg)

    # Output
    print("Forces acting on the ball and their ratios:\n")
    print("Hard kick: {0:10.1f}N\nHard kick ratio: {1:4.1f}N".format(fd_hard_kick, r_hard))
    print("Soft kick: {0:10.1f}N\nSoft kick ratio: {1:4.1f}N".format(fd_soft_kick, r_soft))


if __name__ == '__main__':
    main()

# Terminal Output:
'''
$ python kick.py
Forces acting on the ball and their ratios:

Hard kick:       10.1N
Hard kick ratio:  2.4N
Soft kick:        0.6N
Soft kick ratio:  0.2N
'''
