
def read_file(filename):
    # Crreating empty list
    t_values = []
    with open(filename, 'r') as f:
        # Open with for proper f.close()
        lines = f.read().splitlines()
        nest = [i.split() for i in lines]
        # Making nested list and then creating float and list.
        for ls in nest[2::]:
            for value in ls:
                t_values.append(float(value))
    return float(nest[0][1]), t_values

def file_test():
    # I interpreted the task as: test for object types. Which is to say, does the func()
    # return a float object and a list object.
    # It is also possible to test for the actual values returned.
    with open("test.dat", "w") as f:
        f.write("testval: 42\n")
        f.write("t:\n0.15592  0.28075   0.36807889 0.35 0.57681501876")
    comp = read_file("test.dat")
    expected = 42., [0.15592,  0.28075,   0.36807889, 0.35, 0.57681501876]
    # This success-test could be written as a one-liner,
    # but I think this is nice and readable.
    s1 = type(comp[0]) == type(expected[0])
    s2 = type(comp[1]) == type(expected[1])
    success = s1 and s2
    msg = "expected {}, {} != {}, {} (computed)".format(type(comp[0]), \
                                                type(comp[1]), type(expected[0]), \
                                                type(expected[1]))
    assert success, msg

def write_ty(data):
    # Function uses data from read_file() which has passed the test
    v0 = data[0]
    t = data[1]
    g = 9.81
    # Creating y_values
    y_val = [v0 * i - 0.5 * g * i**2 for i in t]
    with open("table_file.dat", "a") as f:
        # Appending to the file so as not to owerwrite top line.
        # Blanking out the file before writing values.
        f.seek(0)
        f.truncate()
        f.write("{0:^10} {1:^10}\n".format("t", "y")) # top line
        for x, y in zip(t, y_val):
            f.write("{0:^10.3f} {1:^10.3f}\n".format(x, y))

def main():
    # Calling functions and read_file() assigning to data var
    data = read_file("ball.dat")
    file_test()
    write_ty(data)


if __name__ == '__main__':
    main()

# File Output:
'''
I have included the file read by the script.
a) reads file "ball.dat"
b) Creates a new "test_file.dat" or overwrites if allready there.
c) Creates a new "table_file.dat" and appends loop to that file.
'''
