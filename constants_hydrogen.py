
# Read file function: return nested list
def read_file(filename):
    tmp = []
    # We know from exercise instructions that the names we do not need ends with ":"
    with open(filename, "r") as f:
        for lines in f:
            for i, k in enumerate(lines):
                if k == ":":
                    index = i
                    break
            # we append everything after ":" to temporary list
            tmp.append(lines[index+1::])
    # splits items in list in to nested list
    return [i.split() for i in tmp]

# Takes nested list: return dictionary
def nested_to_dict(nested_list):
    const = {}
    for i in nested_list:
        const[i[0]] = float(i[1])
    return const

# Takes dictionary: return float (ref doc-string)
def bohr(d):
    '''
    Function takes a dictionary of constants and
    returns the energy level of a hydrogen atom.
    --------------------------------------------
    '''
    return (((d["ke"]**2)*d["me"]*\
           (d["e"]**4))/\
           (2*(d["hbar"]**2)))

def main():
    # Function calls
    data = read_file("physics_constants.dat")
    const = nested_to_dict(data)
    # Output
    print("{}\n    Calculated value: {}".format(bohr.__doc__, bohr(const)))
    print("    --------------------------------------------")
if __name__ == "__main__":
    main()

# Terminal Output:
'''
$ python constants_hydrogen.py

    Function takes a dictionary of constants and
    returns the energy level of a hydrogen atom.
    --------------------------------------------

    Calculated value: 2.1798723086817252e-18
    --------------------------------------------
'''
