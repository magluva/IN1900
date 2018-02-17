# Importing ball_main module
# It contains one parent calculation class,
# and one test child class.
# It also contains functions that handles input/cmd args.
import ball_main as parent

def main():
    # Calling rt_args from ball_main
    args = parent.rt_args()
    # Creating an instance of the MyCalc class
    obj = parent.MyCalc(float(args[0]), float(args[1]))

    # Printing to screen:
    print("g-value: {}".format(obj.G))
    print("\ny-value: {}".format(obj.calc()))


if __name__ == '__main__':
    print(parent.main.__doc__)
    main()

# Terminal Output:
'''
$ python ball_qa.py

######################################################################
----------------------------------------------------------------------
This script calculates:
y = v0t - 1/2gt^2
----------------------------------------------------------------------
For help on how to run this script with comand line arguments, type:
python ball_main.py --help
----------------------------------------------------------------------

Enter v0-value: 3
Enter t-value: 0.6
g-value: 9.81

y-value: 0.034199999999999786
'''
