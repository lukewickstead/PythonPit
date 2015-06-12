# float_example.py
#
# Float Example
#
# The float type represents a floating point number.
#
# A float is a fixed size representation of a fractional number; it contains digits to the left and right of the
# decimal point.
#
# 1/3 gives us an infinite number of digits after the decimal point which is impossible to store exactly.
#
# Float has a fixed memory size and it's range is represented by significant figures rather than a physical min
# and max boundary. For example 1.0e10 = 10000000000.0 and only has one digit of signification.
#
# Format	        Total bits  Significant bits	Exponent bits
# Single precision	32          23 + 1 sign	        8
# Double precision	64          52 + 1 sign	        11


from sys import getsizeof, float_info

import sys

# Assignment is made with the = operator. Any float value can be used which is a short cut for the float constructor.
print("\n*** Assignment")
x = 1.1
y = float(1.1)

# We can determine the type with the type function
print("\n*** Type")
print(x, type(x))

# We can parse strings to a float including exponential representations.
print("\n*** Passing")
print(float("1"))
print(float("1.0e10"))

# We can round to x d.p
print("\n*** Rounding")
print(round(1.11111, 2))

# We can perform many maths operators
# See ../Operators/*.py for more details
print("\n*** Operators")
print(1.1 + 1.1)
print(1.1 - 1.1)
print(1.1 / 1.1)
print(1.1 * 1.1)

print("\n*** Float information")
print(float_info)
print(sys.float_info.min)
print(sys.float_info.max)

# For 64 bit machines we have 53 bits of signification which includes the sign


# The memory is always fixed as 24 bytes
print("\n*** Size")
print(getsizeof(float(0)))
print(getsizeof(1.1))
print(getsizeof(float(9999999.9)))
# print(getsizeof(1.1**1024.1)) # Causes OverflowError: (34, 'Numerical result out of range')


# Accuracy; as per all languages and systems floats are approximations and as such suffer from accuracy.
print("\n*** Accuracy ")
print(1 / 3)
print(.1 + .1 + .1 == .3)
print(float(.1) + float(.1) + float(.1))


# The following pages explain floats and their inherent issue.
# http://floating-point-gui.de/languages/python/
# http://en.wikipedia.org/wiki/Floating_point
# https://docs.python.org/2/tutorial/floatingpoint.html
