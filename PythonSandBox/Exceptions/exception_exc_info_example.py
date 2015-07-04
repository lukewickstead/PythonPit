# exception_exc_info_example.py
#
# Exception Exc Info Example
#
# sys.exc_info provides a tuple of information about the current exception being raised.

import sys

# noinspection PyBroadException,PyBroadException
try:
    f = open('foo.txt')
    s = f.readline()
    i = int(s.strip())
except:
    print("Catch!!")
    for a_msg in sys.exc_info():
        print(a_msg)
