import sys
import argparse


class MyCalc:
    # Defining class with G as constant attribute.
    G = 9.81

    # Avoiding __dict__ attributes (saves memory wit few passed attributes)
    __slots__ = ["v0", "t"]
    def __init__(self, v0, t):
        self.v0 = v0
        self.t = t

    # Defining the workhorse of the script
    def calc(self):
        return self.v0*self.t - 0.5*self.G*self.t**2


class MyCalcTest(MyCalc):
    # Defining test subclass. Here we can also add a test for the parser etc.
    __slots__ = ["v0", "t"]
    def __init__(self, v0, t):
        super(MyCalcTest, self).__init__(v0, t)

    # Defining test function with fixed values.
    def test_fixed(self):
        test = MyCalc(3, 0.6)
        expected = 0.034199999999999786
        computed = test.calc()
        tol = 1E-14
        success = abs(computed - expected) < tol
        if success:
            return "test_fixed() ... ok"
        return "test_fixed() ... failed"

    def test_dynamic(self):
        test = MyCalc(self.v0, self.t)
        g = test.G
        expected = self.v0*self.t - 0.5*g*self.t**2
        computed = test.calc()
        tol = 1E-14
        success = abs(computed - expected) < tol
        if success:
            return "test_dynamic() ... ok"
        return "test_dynamic() ... failed"


def cmd_args(args):
    # defining command line positional args
    parser = argparse.ArgumentParser()
    parser.add_argument("-v","--v0value", nargs="?", action="store", type=float,
                       help=" Provide a v-value for the calculation")
    parser.add_argument("-t", "--tvalue", nargs="?", action="store", type=float,
                       help=" Provide a t-value for the calculation")
    # unpacking Namespace() and coverts to list to match rt_args
    # to avoid code duplication in main()
    args = parser.parse_args()
    return [args.v0value, args.tvalue]

def rt_args():
    # Asking for args. Only used if cmd-args were not provided
    v0 = input("Enter v0-value: ")
    t = input("Enter t-value: ")
    args = [v0, t]
    return args

def event_handler():
    # if no cmd args were passed the script will ask for values
    print("Checking for command line arguments ...")
    args = cmd_args(sys.argv[1::])
    if args == [None, None]:
        print("Not found!\n")
        return rt_args()
    print("found!")
    return args

def lim_check(args):
    lim_min = 0
    lim_max = (2*float(args[0]))/9.81
    if not lim_min < float(args[1]) < lim_max:
        print("Values must be between 0 and 2*v0/g")
        return True
    return False

def main():
    # Docstring with basic script info
    '''
######################################################################
----------------------------------------------------------------------
This script calculates:
y = v0t - 1/2gt^2
----------------------------------------------------------------------
For help on how to run this script with comand line arguments, type:
python ball_main.py --help
----------------------------------------------------------------------
    '''
    # Declaring exception_handler function()
    args = event_handler()
    # Checks if user entered any args at all capable of being "converted" to float
    try:
        obj = MyCalc(float(args[0]), float(args[1]))
    except:
        print("No (or too few) arguments were provided either from cmd at execution or during input stage.")
        print("exiting ..."); sys.exit(2)

    # Main Output
    print("----------------------------------------------------------------------")
    print("Values: v0 = {}, t = {}, g = {}".format(args[0], args[1], obj.G))
    print("The calculated value is: {}".format(obj.calc()))

    print("")
    print("----------------------------------------------------------------------")
    # Checks for successfull test child class __init__ and method usage
    try:
        test = MyCalcTest(float(args[0]), float(args[1]))
        # Prints test results
        print(test.test_fixed())
        print(test.test_dynamic())
    except:
        print("Error: Occured while calling MyCalcTest class. Back to work!")

if __name__ == '__main__':
    # Prints main() docstring with a greeting.
    print(main.__doc__)
    main()
