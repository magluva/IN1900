# Importing ball_main
import ball_main as parent
import sys

def main():

     # calling event_handler function() from ball_main
    args = parent.event_handler()

    try:
        # Checks if lim_check() returns True.
        # Will ask for input until it return False (This means accepted values)
        while parent.lim_check(args):
            args = parent.rt_args()

        # Checks if user entered any args at all capable of being "converted" to float

        obj = parent.MyCalc(float(args[0]), float(args[1]))
    except:
        print("No (or too few) arguments were provided either from cmd at execution or during input stage.")
        print("exiting ..."); sys.exit(2)

    # Prints to screen:
    print("")
    print("v0-value: {}".format(args[0]))
    print("t-value: {}".format(args[1]))
    print("g-value: {}".format(obj.G))
    print("\ny-value: {}".format(obj.calc()))


if __name__ == '__main__':
    print(parent.main.__doc__)
    main()

# Terminal Output:
'''

######################################################################
----------------------------------------------------------------------
This script calculates:
y = v0t - 1/2gt^2
----------------------------------------------------------------------
For help on how to run this script with comand line arguments, type:
python ball_main.py --help
----------------------------------------------------------------------

Checking for command line arguments ...
found!
Values must be between 0 and 2*v0/g
Enter v0-value: 3
Enter t-value: 0.6

v0-value: 3
t-value: 0.6
g-value: 9.81

y-value: 0.034199999999999786
'''
