# Importing ball_main module
import ball_main as parent
import sys

def main():
    # Calling cmd_args() from ball_main
    args = parent.cmd_args(sys.argv[1::])
    # Creating an instance of the MyCalc class
    obj = parent.MyCalc(float(args[0]), float(args[1]))

    # Printing to screen:
    print("v0-value: {}".format(args[0]))
    print("t-value: {}".format(args[1]))
    print("g-value: {}".format(obj.G))
    print("\ny-value: {}".format(obj.calc()))


if __name__ == '__main__':
    print(parent.main.__doc__)
    main()

# Terminal Output:
'''
$python ball_cml.py -v 3 -t 0.6

######################################################################
----------------------------------------------------------------------
This script calculates:
y = v0t - 1/2gt^2
----------------------------------------------------------------------
For help on how to run this script with comand line arguments, type:
python ball_main.py --help
----------------------------------------------------------------------

v0-value: 3.0
t-value: 0.6
g-value: 9.81

y-value: 0.034199999999999786
'''
