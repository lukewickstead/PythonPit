# exception_exc_infoexample.py
#
# Exception Exc Info Example
#

import sys

try:
    f = open('foo.txt')
    s = f.readline()
    i = int(s.strip())
except:
    print("Catch!!")
    for a_msg in sys.exc_info():
        print(a_msg)