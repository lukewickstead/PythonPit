# math_example.py
#
# Math Example
#
# The math module contains various useful basic maths functions.
#
# There are many third party math modules which should considered where applicable:
#
# SciPy:      http://scipy.org
# NumPy:      http://www.numpy.org/
#

import math

print("math.ceil(11.11):", math.ceil(11.11))                        # Ceiling'
print("math.floor(11.11):", math.floor(11.11))                      # Floor
print("math.pi:", math.pi)                                          # Pi
print("math.fabs(-999):", math.fabs(-999))                          # Abs
print("math.trunc(1.11):", math.trunc(1.11))                        # Truncate
print("math.fsum([1, 2, 3]):", math.fsum([1, 2, 3]))                # Sums an enumerable
print("math.isfinite(1):", math.isfinite(1))                        # Not infinite
print("math.isinf(float('inf')):", math.isinf(float("inf")))        # Infinite
print("math.isnan(float('inf'')):", math.isnan(float("inf")))       # Not NaN
print("math.pow(3, 3):", math.pow(3, 3))                            # To the power of
print("math.sqrt(9):", math.sqrt(9))                                # Square root
print("math.radians(360):", math.radians(360))                      # Degrees to Radian
print("math.degrees(6.28...):", math.degrees(6.283185307179586))    # Radians to degrees