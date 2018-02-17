
s = 0; k = 1; M = 100;

# while k < M:
#   s += 1/k
#
# print s


while k <= M:
    s += 1/k
    k += 1

print(s)

# Errors & Fixes starting at line:
'''
1) M needs to be 101 or you ned to change the "smaller than"
operator to a "smaller than or equal to" operator.
This is so you include the MAX value.

2) k must be incremented for each iteration or it will be an
infinite loop!

3) Since parenthesis was omitted from the print statement
I suspect this was made in python 2 where integer division was
standard. Change datatype to float by adding a . at the end of the values or
import division from __future__ and run witu -i flag.
In python >= 3 int has been changed to long and float (true) division is
standard. You can still do integer division with "//" (floor division).
'''

# Terminal Output:
'''
$ python sum_while.py
5.187377517639621
'''
