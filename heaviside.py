
# Defining Heaviside function()
def H(x):
    if x < 0:
        return 0
    else:
        return 1

# Defining test function()
def H_test():
    values = [-10, -10**-15, 0, 10**15, 10]
    expected = [0, 0, 1, 1, 1]
    computed = [H(i) for i in values]
    tol = 1E-14
    # Looping throug and asserting expected values.
    for e, c in zip(expected, computed):
        success = abs(e - c) < tol
        msg = "expected {} != {} (computed)".format(e, c)
        assert success, msg

def main():

    # Calling test function()
    H_test()

    print("\n------------------------------------------")
    print("H_test() ... ok\n")

if __name__ == '__main__':
    main()

# Terminal Output:
'''
$ python heaviside.py

------------------------------------------
H_test() ... ok

'''
# Terminal Output H_test() Falure Example:
'''
$ python heaviside.py
Traceback (most recent call last):
  File "heaviside.py", line 26, in <module>
    main()
  File "heaviside.py", line 20, in main
    H_test()
  File "heaviside.py", line 16, in H_test
    assert success, msg
AssertionError: expected 0 != 1 (computed)
'''
