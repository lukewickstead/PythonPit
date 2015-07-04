# int_example.py
#
# Int Example
#
# In Python < 3 there were int and long instances. Ints have a defined range, long are infinite but dependant upon the
# size of the available memory.
#
# In Python >=3 the int and long are merged into an int class. The runtime handles determining the memory size based
# upon the size of the integer being represented.

from sys import getsizeof

import sys

# Assignment is made with the = operator. Any integer value can be used which is a short cut for the int constructor.
print("\n*** Assignment")
x = 1
y = int(1)

# We can determine the type with the type function
print("\n*** Type")
print(x, type(x))

# We can parse strings to an int
print("\n*** Passing")
x = int("1")

# We can check that a string only contains characters which can be parsed
print(str.isdigit("1"))
print(str.isdigit("a"))

# We can round by passing in a negative d.p.
print("\n*** Rounding")
print(round(11111, -2))

# We can perform many maths operators
# See ../Operators/*.py for more details
print("\n*** Operators")
print(1 + 1)
print(1 - 1)
print(1 / 1)
print(1 * 1)

# Int information
print("\n*** Int information")
print(print(sys.int_info))

# This will vary depending if you are using 32bit/64bit
# sys.int_info(bits_per_digit=30, sizeof_digit=4)
# sys.int_info(bits_per_digit=15, sizeof_digit=2)

# 64 bit systems will store a digit as 2**30 bits.
# 32 bit systems will store a digit as 2*15 bits
# Both will allow ints to grow to an infinite size dependant on memory.

# The memory used is dependant upon what is required.
print("\n*** Size")
print(getsizeof(0))
print(getsizeof(100 ** 100))
print(getsizeof(100 ** 100100))
