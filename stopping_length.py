import sys

def life_saver(v0, u):
    # Defining math function(). takes lists as args and
    # returns a list of d values.
    d = []
    for v_val, u_val in zip(v0, u):
        g = 9.81
        v0 = v_val/3.6

        u = u_val
        d.append((1/2)*((v0**2)/(u*g)))
    return d


def main():
    # Informative docstring.
    '''
-----------------------------------------------------------
This script takes an arbitrary number of v0 and u cmd args
and prints the answers to screen.
If no cmd args ar specified the user will be asked to
provide exactly one v0 argument and exactly one u argument.
-----------------------------------------------------------
    '''

    try:
        args = [float(arg) for arg in sys.argv[1::]]
        # Here we can use a try and except block, but i chose if/else
        # flow control. There are viritually no speed difference between the
        # two for small blocks.
        if not len(args) < 2:
            v0 = [v for v in args[::2]]
            u = [u for u in args[1::2]]
        else:
            try:
                # Try/except for missing values
                print("Missing cmd arguments.")
                v0 = [float(input("Please enter v0: "))]
                u = [float(input("Please enter u: "))]
            except ValueError:
                print("No args were given")
                print("Exiting ..."); sys.exit(2)

        # Print to screen
        print("Your calculated values:")
        [print(d) for d in life_saver(v0, u)]

    except KeyboardInterrupt:
        print("\nHow rude!")
        # I know... He ruined the prequels.


if __name__ == '__main__':
    print(main.__doc__)
    main()

# Terminal Output:
'''
$ python stopping_length.py 120 0.3 50 0.3

-----------------------------------------------------------
This script takes an arbitrary number of v0 and u cmd args
and prints the answers to screen.
If no cmd args ar specified the user will be asked to
provide exactly one v0 argument and exactly one u argument.
-----------------------------------------------------------

Your calculated values:
188.77185034167707
32.77289068431893

'''
