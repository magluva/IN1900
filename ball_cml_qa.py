# Importing ball_main module
import ball_main as parent
import sys

def main():

     # Calling event_handler() from ball_main
    args = parent.event_handler()
    # Checks if user entered any args at all capable of being "converted" to float
    try:
        # Tries to create MyCalc object.
        obj = parent.MyCalc(float(args[0]), float(args[1]))
    except:
        # Exit if "object creation" fails
        print("No (or too few) arguments were provided either from cmd at execution or during input stage.")
        print("exiting ..."); sys.exit(2)

    # Print to screen:
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
$ python ball_cml_qa.py

######################################################################
----------------------------------------------------------------------
This script calculates:
y = v0t - 1/2gt^2
----------------------------------------------------------------------
For help on how to run this script with comand line arguments, type:
python ball_main.py --help
----------------------------------------------------------------------

Checking for command line arguments ...
Not found!

Enter v0-value: 3
Enter t-value: 0.6

v0-value: 3
t-value: 0.6
g-value: 9.81

y-value: 0.034199999999999786
'''
# Wit cmd args
'''
$ python ball_cml_qa.py -v 6 -t 0.6

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

v0-value: 6.0
t-value: 0.6
g-value: 9.81

y-value: 1.8341999999999996
'''
